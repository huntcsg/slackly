Slack Events
============

.. automodule:: slackly.events

Base Classes and Utilities
--------------------------

.. autoclass:: slackly.events._base.BaseEvent

.. py:function:: slackly.events._base.register_event

Events
------

.. autoclass:: slackly.events.accounts_changed.AccountsChanged
.. autoclass:: slackly.events.bot_added.BotAdded
.. autoclass:: slackly.events.accounts_changed.AccountsChanged
.. autoclass:: slackly.events.bot_added.BotAdded
.. autoclass:: slackly.events.bot_changed.BotChanged
.. autoclass:: slackly.events.channel_archive.ChannelArchive
.. autoclass:: slackly.events.channel_created.ChannelCreated
.. autoclass:: slackly.events.channel_deleted.ChannelDeleted
.. autoclass:: slackly.events.channel_history_changed.ChannelHistoryChanged
.. autoclass:: slackly.events.channel_joined.ChannelJoined
.. autoclass:: slackly.events.channel_left.ChannelLeft
.. autoclass:: slackly.events.channel_marked.ChannelMarked
.. autoclass:: slackly.events.channel_rename.ChannelRename
.. autoclass:: slackly.events.channel_unarchive.ChannelUnarchive
.. autoclass:: slackly.events.commands_changed.CommandsChanged
.. autoclass:: slackly.events.desktop_notification.DesktopNotification
.. autoclass:: slackly.events.dnd_updated.DndUpdated
.. autoclass:: slackly.events.dnd_updated_user.DndUpdatedUser
.. autoclass:: slackly.events.email_domain_changed.EmailDomainChanged
.. autoclass:: slackly.events.emoji_changed.EmojiChanged
.. autoclass:: slackly.events.file_change.FileChange
.. autoclass:: slackly.events.file_comment_added.FileCommentAdded
.. autoclass:: slackly.events.file_comment_deleted.FileCommentDeleted
.. autoclass:: slackly.events.file_comment_edited.FileCommentEdited
.. autoclass:: slackly.events.file_created.FileCreated
.. autoclass:: slackly.events.file_deleted.FileDeleted
.. autoclass:: slackly.events.file_public.FilePublic
.. autoclass:: slackly.events.file_shared.FileShared
.. autoclass:: slackly.events.file_unshared.FileUnshared
.. autoclass:: slackly.events.goodbye.Goodbye
.. autoclass:: slackly.events.group_archive.GroupArchive
.. autoclass:: slackly.events.group_close.GroupClose
.. autoclass:: slackly.events.group_history_changed.GroupHistoryChanged
.. autoclass:: slackly.events.group_joined.GroupJoined
.. autoclass:: slackly.events.group_left.GroupLeft
.. autoclass:: slackly.events.group_marked.GroupMarked
.. autoclass:: slackly.events.group_open.GroupOpen
.. autoclass:: slackly.events.group_rename.GroupRename
.. autoclass:: slackly.events.group_unarchive.GroupUnarchive
.. autoclass:: slackly.events.hello.Hello
.. autoclass:: slackly.events.im_close.ImClose
.. autoclass:: slackly.events.im_created.ImCreated
.. autoclass:: slackly.events.im_history_changed.ImHistoryChanged
.. autoclass:: slackly.events.im_marked.ImMarked
.. autoclass:: slackly.events.im_open.ImOpen
.. autoclass:: slackly.events.manual_presence_change.ManualPresenceChange
.. autoclass:: slackly.events.member_joined_channel.MemberJoinedChannel
.. autoclass:: slackly.events.message.Message
.. autoclass:: slackly.events.pin_added.PinAdded
.. autoclass:: slackly.events.pin_removed.PinRemoved
.. autoclass:: slackly.events.pong.Pong
.. autoclass:: slackly.events.pref_change.PrefChange
.. autoclass:: slackly.events.presence_change.PresenceChange
.. autoclass:: slackly.events.reaction_added.ReactionAdded
.. autoclass:: slackly.events.reaction_removed.ReactionRemoved
.. autoclass:: slackly.events.reconnect_url.ReconnectUrl
.. autoclass:: slackly.events.star_added.StarAdded
.. autoclass:: slackly.events.star_removed.StarRemoved
.. autoclass:: slackly.events.subteam_created.SubteamCreated
.. autoclass:: slackly.events.subteam_self_added.SubteamSelfAdded
.. autoclass:: slackly.events.subteam_self_removed.SubteamSelfRemoved
.. autoclass:: slackly.events.subteam_updated.SubteamUpdated
.. autoclass:: slackly.events.team_domain_change.TeamDomainChange
.. autoclass:: slackly.events.team_join.TeamJoin
.. autoclass:: slackly.events.team_migration_started.TeamMigrationStarted
.. autoclass:: slackly.events.team_plan_change.TeamPlanChange
.. autoclass:: slackly.events.team_pref_change.TeamPrefChange
.. autoclass:: slackly.events.team_profile_change.TeamProfileChange
.. autoclass:: slackly.events.team_profile_delete.TeamProfileDelete
.. autoclass:: slackly.events.team_profile_reorder.TeamProfileReorder
.. autoclass:: slackly.events.team_rename.TeamRename
.. autoclass:: slackly.events.thread_marked.ThreadMarked
.. autoclass:: slackly.events.thread_subscribed.ThreadSubscribed
.. autoclass:: slackly.events.thread_unsubscribed.ThreadUnsubscribed
.. autoclass:: slackly.events.update_thread_state.UpdateThreadState
.. autoclass:: slackly.events.url_verification.UrlVerification
.. autoclass:: slackly.events.user_change.UserChange
.. autoclass:: slackly.events.user_typing.UserTyping
