# encoding: utf-8

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from event_log import registry


registry.register(
    name='shoottikala.photographer.created',
    message=_('Photographer signed up: {entry.photographer.display_name}'),
)

registry.register(
    name='shoottikala.cosplayer.created',
    message=_('Cosplayer signed up: {entry.cosplayer.display_name}'),
)
