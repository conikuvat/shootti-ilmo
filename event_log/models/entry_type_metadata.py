# encoding: utf-8

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _


class EntryTypeMetadata(object):
    def __init__(
        self,
        name,
        message=lambda entry: _('An event of type {entry.entry_type} occurred').format(entry=entry),
        email_body_template='event_log_default.eml',
        email_reply_to=None,
    ):
        self.name = name
        self.message = message
        self.email_body_template = email_body_template
        self.email_reply_to = email_reply_to

    def __str__(self):
        return self.name
