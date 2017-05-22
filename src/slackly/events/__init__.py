"""This package contains all events"""
from ._base import register_event, event_registry

from .bot_added import BotAdded
from .bot_changed import BotChanged
from .channel_archive import ChannelArchive
from .channel_created import ChannelCreated
from .channel_deleted import ChannelDeleted
from .channel_history_changed import ChannelHistoryChanged
from .channel_joined import ChannelJoined
from .channel_left import ChannelLeft
from .channel_marked import ChannelMarked
from .channel_rename import ChannelRename
from .channel_unarchive import ChannelUnarchive
from .commands_changed import CommandsChanged
from .desktop_notification import DesktopNotification
from .dnd_updated import DndUpdated
from .dnd_updated_user import DndUpdatedUser
from .email_domain_changed import EmailDomainChanged
from .emoji_changed import EmojiChanged
from .file_change import FileChange
from .file_comment_added import FileCommentAdded
from .file_comment_deleted import FileCommentDeleted
from .file_comment_edited import FileCommentEdited
from .file_created import FileCreated
from .file_deleted import FileDeleted
from .file_public import FilePublic
from .file_shared import FileShared
from .file_unshared import FileUnshared
from .goodbye import Goodbye
from .group_archive import GroupArchive
from .group_close import GroupClose
from .group_history_changed import GroupHistoryChanged
from .group_joined import GroupJoined
from .group_left import GroupLeft
from .group_marked import GroupMarked
from .group_open import GroupOpen
from .group_rename import GroupRename
from .group_unarchive import GroupUnarchive
from .hello import Hello
from .im_close import ImClose
from .im_created import ImCreated
from .im_history_changed import ImHistoryChanged
from .im_marked import ImMarked
from .im_open import ImOpen
from .manual_presence_change import ManualPresenceChange
from .message import Message
from .pin_added import PinAdded
from .pin_removed import PinRemoved
from .pong import Pong
from .pref_change import PrefChange
from .presence_change import PresenceChange
from .reaction_added import ReactionAdded
from .reaction_removed import ReactionRemoved
from .reconnect_url import ReconnectUrl
from .star_added import StarAdded
from .star_removed import StarRemoved
from .subteam_created import SubteamCreated
from .subteam_self_added import SubteamSelfAdded
from .subteam_self_removed import SubteamSelfRemoved
from .subteam_updated import SubteamUpdated
from .team_domain_change import TeamDomainChange
from .team_join import TeamJoin
from .team_migration_started import TeamMigrationStarted
from .team_plan_change import TeamPlanChange
from .team_pref_change import TeamPrefChange
from .team_profile_change import TeamProfileChange
from .team_profile_delete import TeamProfileDelete
from .team_profile_reorder import TeamProfileReorder
from .team_rename import TeamRename
from .thread_marked import ThreadMarked
from .thread_subscribed import ThreadSubscribed
from .thread_unsubscribed import ThreadUnsubscribed
from .update_thread_state import UpdateThreadState
from .url_verification import UrlVerification
from .user_change import UserChange
from .user_typing import UserTyping
