#!/usr/bin/python3
from .compat import BaseHTTPRequestHandler, HTTPServer
import urllib
import json
import sys
import time
import warnings

from slackly import SlackClient


warnings.warn("This part of slackly (oauth_utils) is highly experimental and will likely see api breaking changes")


class CodeServer(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)
        host, query = urllib.parse.splitquery(self.path)
        query_values = urllib.parse.parse_qs(query)
        if 'code' in query_values:
            query_values['code'] = query_values['code'][0]
        if 'state' in query_values:
            query_values['state'] = query_values['state'][0]
            if query_values['state'] != self.state_validate:
                print("Not a valid request")
                return

        print(json.dumps(query_values, indent=4))

        client = SlackClient()
        response = client.api.oauth.access(
            client_id=client_id,
            client_secret=client_secret,
            code=query_values['code'],
            redirect_uri=redirect_uri,
        )

        print(json.dumps(response.data, indent=4))
        return


def main(host, port, state, client_id, client_secret, redirect_uri):
    CodeServer.state_validate = state
    server = HTTPServer((host, port), CodeServer)

    print(time.asctime(), "Server Starts - %s:%s" % (host, port))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (host, port))


if __name__ == '__main__':
    host = sys.argv[1]
    port = int(sys.argv[2])
    state = sys.argv[3]
    client_id = sys.argv[4]
    client_secret = sys.argv[5]
    redirect_uri = sys.argv[6]

    main(host, port, state, client_id, client_secret, redirect_uri)
