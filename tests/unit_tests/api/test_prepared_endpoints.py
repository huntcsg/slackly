from unittest import TestCase
from slackly.api.endpoints._base import BaseAPIEndpoint, BaseAPIDispatch, SlackAPICall


def call_end_points(dispatcher):
    calls = []
    for attr in vars(dispatcher.__class__).values():
        if isinstance(attr, BaseAPIEndpoint):
            fake_kwargs = {arg: 'DUMMY' for arg in attr.required_args}
            fake_optional_kwargs = {arg: 'DUMMY' for arg in attr.optional_args}
            fake_optional_kwargs.update(fake_kwargs)
            # Make the prepared call

            calls.append((
                attr.endpoint,
                lambda self, attr=attr, fake_kwargs=fake_kwargs: self.assertIsInstance(attr(**fake_kwargs), SlackAPICall),
                lambda self, attr=attr, fake_optional_kwargs=fake_optional_kwargs: self.assertIsInstance(attr(**fake_optional_kwargs), SlackAPICall),
                lambda self, attr=attr: repr(attr),
            ))

        elif isinstance(attr, BaseAPIDispatch):
            calls.extend(call_end_points(attr))

    return calls

class TestPreparedCalls(TestCase):

    from slackly import SlackAPI
    api = SlackAPI()

    calls = []
    calls.extend(call_end_points(api))
    for endpoint, callable_test_required_args, callable_test_optional_args, repr_test in calls:
        endpoint_str = endpoint.replace('.', '_')
        locals()["test_prepared_call_required_only_{}".format(endpoint_str)] = callable_test_required_args
        locals()["test_prepared_call_optional_{}".format(endpoint_str)] = callable_test_optional_args
        locals()["test_endpoint_repr_{}".format(endpoint_str)] = repr_test