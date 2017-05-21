from websocket import create_connection
from ssl import SSLError
import json
import queue
from threading import Thread

from .event_factory import SlackEventDict


def send_messages(q, websocket, keep_alive=True):
    ping_msg = json.dumps({'type': 'ping'}).encode('utf-8')
    while True:
        try:
            msg = q.get(timeout=3)
            websocket.send(msg)
        except queue.Empty:
            if keep_alive:
                websocket.send(ping_msg)


def recieve_messages(q, websocket, ignore_pong=True):
    while True:
        try:
            msg = json.loads(websocket.recv())
            if msg['type'] == 'pong' and ignore_pong:
                continue
            else:
                q.put(msg)
        except SSLError as e:
            if e.errno == 2:
                continue
            raise


class SlackRTMClient(object):

    def __init__(self, token, url, event_factory=SlackEventDict, client=None, keep_alive=True, ignore_pong=True):
        if client is None:
            from .api_client import SlackClient
            client = SlackClient(token=token)

        self.client = client
        self.token = token
        self.url = url
        self.event_factory = event_factory

        self.websocket = None
        self.send_queue = queue.Queue()
        self.send_daemon = None
        self.keep_alive = keep_alive

        self.receive_queue = queue.Queue()
        self.receive_daemon = None
        self.ignore_pong = ignore_pong

    @classmethod
    def from_response(cls, endpoint, token, response):
        url = response['url']
        rtm_client = cls(token=token, url=url)
        rtm_client.connect()

        return rtm_client

    @classmethod
    def from_token(cls, token):
        from .api_client import SlackClient
        from ..api import SlackAPI
        client = SlackClient(token=token)
        api = SlackAPI()
        api.bind = client
        return api.rtm.connect()

    @classmethod
    def from_client(cls, client):
        from ..api import SlackAPI
        api = SlackAPI()
        api.bind = client
        rtm_client = api.rtm.connect()
        rtm_client.client = client
        return rtm_client

    def connect(self):
        self.websocket = create_connection(self.url)
        self.websocket.sock.setblocking(True)

        self.send_daemon = Thread(target=send_messages, args=(self.send_queue, self.websocket, self.keep_alive), daemon=True)
        self.send_daemon.start()

        self.receive_daemon = Thread(target=recieve_messages, args=(self.receive_queue, self.websocket), daemon=True)
        self.receive_daemon.start()

    def get_event(self, timeout=None):
        try:
            return self.event_factory(self.receive_queue.get(timeout=timeout))
        except queue.Empty:
            pass

    def get_events_forever(self):
        while True:
            yield self.get_event()

    def send_event(self, event):
        event_bytes = json.dumps(event).encode('utf-8')
        self.send_queue.put(event_bytes)
