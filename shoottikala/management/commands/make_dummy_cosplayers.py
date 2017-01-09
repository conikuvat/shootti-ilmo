import logging
from random import choice

from django.core.management.base import BaseCommand

from kompassi_oauth2.models import User

from ...models import Cosplayer, Event
from ...utils import log_get_or_create


logger = logging.getLogger(__name__)

USERNAME_LENGTH = 8


class Command(BaseCommand):
    args = ''
    help = 'Import an event from Kompassi'

    def add_arguments(self, parser):
        parser.add_argument('event_slug', type=str)
        parser.add_argument('num_dummies', default=3, type=int)

    def handle(self, *args, **options):
        event = Event.objects.get(slug=options['event_slug'])

        for i in range(options['num_dummies']):
            username = ''.join(choice('xrnmvz') for i in range(USERNAME_LENGTH))
            user, unused = User.get_or_create_dummy(username=username)
            cosplayer, created = Cosplayer.get_or_create_dummy(user=user, event=event)
            log_get_or_create(logger, cosplayer, created)
