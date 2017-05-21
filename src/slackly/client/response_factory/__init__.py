import json


class SlackAPIDictResponse(object):

    def __init__(self, endpoint, response, raise_for_status=False):
        # Thanks Slacker for the inspiration
        if raise_for_status:
            response.raise_for_status()

        self.endpoint = endpoint
        self.data = response.json()

        self.successful = self.data['ok']
        self.warnings = self.data.get('response_metadata', {}).get('warnings', [])
        self.error = self.data.get('error', None)

    def __repr__(self):
        return json.dumps(self.data)
