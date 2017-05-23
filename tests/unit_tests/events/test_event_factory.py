from unittest import TestCase
import os
import json

class TestEventObjectFactory(TestCase):

    def setUp(self):
        from slackly.events._base import BaseEvent
        self.base_event = BaseEvent

    def callFUT(self, event):
        from slackly import SlackEventParsed
        return SlackEventParsed(event)

    events_data_dir = 'tests/data/events'
    for event in os.listdir(events_data_dir):
        event_dir = os.path.join(events_data_dir, event)
        for file in os.listdir(event_dir):
            def test_func(self, event_dir=event_dir, file=file, event=event):
                with open(os.path.join(event_dir, file), 'rb') as f:
                    event_data = json.loads(f.read().decode('utf-8'))
                    result = self.callFUT(event_data)
                    self.assertIsInstance(result, self.base_event)

            case_name = file.replace('.json', '')

            locals()['test_{}_{}'.format(event, case_name)] = test_func

class TestEventDictFactory(TestCase):

    def setUp(self):
        from slackly.events._base import BaseEvent
        import slackly.events
        self.base_event = BaseEvent

    def callFUT(self, event):
        from slackly import SlackEventDict
        return SlackEventDict(event)

    events_data_dir = 'tests/data/events'
    for event in os.listdir(events_data_dir):
        event_dir = os.path.join(events_data_dir, event)
        for file in os.listdir(event_dir):
            def test_func(self, event_dir=event_dir, file=file, event=event):
                with open(os.path.join(event_dir, file), 'rb') as f:
                    event_data = json.loads(f.read().decode('utf-8'))
                    result = self.callFUT(event_data)
                    self.assertIsInstance(result, dict)
                    self.assertIsInstance(result, self.base_event)

            case_name = file.replace('.json', '')

            locals()['test_{}_{}'.format(event, case_name)] = test_func