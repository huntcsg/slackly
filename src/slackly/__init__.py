__version__ = '1.0.0'
from .config import get_config_value

from .client import (
    SlackClient,
    SlackRTMClient,
    SlackAPIDictResponse,
    SlackAPIObjectResponse,
    SlackEventDict,
    SlackEventParsed,
)

from .api import SlackAPI
from . import events
from .schema import types
from .schema.types import (
    SlackType,

    Message,
    User,
    Channel,
    Team,
    IM,
    MPIM,
    File,
    FileComment,
)
