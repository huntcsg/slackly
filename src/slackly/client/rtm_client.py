import json
import logging
import ssl
import threading
import websocket

from ..compat import queue
from .event_factory import SlackEventDict


def send_messages(q, websocket, keep_alive=True, donotdie=True):
    logger = logging.getLogger(__name__)

    ping_msg = json.dumps({'type': 'ping'}).encode('utf-8')
    while True:
        try:
            msg = q.get(timeout=3)
            websocket.send(msg)
            raise RuntimeError
        except queue.Empty:
            if keep_alive:
                websocket.send(ping_msg)
        except Exception as e:
            if donotdie:
                logger.debug("Something went wrong in the message sender: {}".format(e), exc_info=True)
                continue
            else:
                logger.exception(e)
                raise e


def receive_messages(q, websocket, ignore_pong=True, donotdie=True):
    logger = logging.getLogger(__name__)
    while True:
        try:
            msg = json.loads(websocket.recv())
            if msg['type'] == 'pong' and ignore_pong:
                continue
            else:
                q.put(msg)
            raise RuntimeError
        except ssl.SSLError as e:
            if e.errno == 2:
                logger.debug("Something went wrong in the message receiver: {}".format(e), exc_info=True)
                continue
        except Exception as e:
            if donotdie:
                logger.debug("Something went wrong in the message receiver: {}".format(e), exc_info=True)
                continue
            else:
                logger.exception(e)
                raise e


class SlackRTMClient(object):
    """The RTM Client
    
    """

    def __init__(self, token, url, event_factory=SlackEventDict, client=None, keep_alive=True, ignore_pong=True, donotdie=True):
        """
        
        :param token: A :class:`str` token
        :param url: A :class:`str` the base url for slack
        :param event_factory: A class to process events coming off the real time messaging api
        :param client: A :class:`slackly.SlackClient` or None.
        :param keep_alive: The option to have the websocket automatically written to at least every 3 seconds
        :param ignore_pong: Whether to emit or squash the response to pings
        """
        if client is None:
            from .api_client import SlackClient
            client = SlackClient(token=token)

        self.client = client
        self.token = token
        self.url = url
        self.event_factory = event_factory

        self.donotdie = True

        self.websocket = None
        self.send_queue = queue.Queue()
        self.send_daemon = None
        self.keep_alive = keep_alive

        self.receive_queue = queue.Queue()
        self.receive_daemon = None
        self.ignore_pong = ignore_pong

        self.connected = False

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
        self.websocket = websocket.create_connection(self.url)
        self.websocket.sock.setblocking(True)

        self.send_daemon = threading.Thread(target=send_messages, args=(self.send_queue, self.websocket, self.keep_alive, self.donotdie), daemon=True)
        self.send_daemon.start()

        self.receive_daemon = threading.Thread(target=receive_messages, args=(self.receive_queue, self.websocket, self.donotdie), daemon=True)
        self.receive_daemon.start()
        self.connected = True

    def get_event(self, timeout=None):
        try:
            return self.event_factory(self.receive_queue.get(timeout=timeout))
        except queue.Empty:
            pass

    def get_events(self):
        while True:
            try:
                yield self.event_factory(self.receive_queue.get(block=False))
            except queue.Empty:
                break

    def get_events_forever(self):
        while True:
            yield self.get_event()

    def send_event(self, event):
        event_bytes = json.dumps(event).encode('utf-8')
        self.send_queue.put(event_bytes)

    def __repr__(self):
        inbox = self.receive_queue.qsize()
        outbox = self.send_queue.qsize()
        token = "...{}".format(self.token[-5:])
        return "{cls.__class__.__name__}(token='{token}' | " \
               "connected: {cls.connected} | " \
               "inbox: {inbox} | " \
               "outbox: {outbox})".format(cls=self, token=token, inbox=inbox, outbox=outbox)
