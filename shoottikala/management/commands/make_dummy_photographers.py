import logging
from random import choice

from django.core.management.base import BaseCommand

from kompassi_oauth2.models import User

from ...models import Photographer, Event
from ...utils import log_get_or_create


logger = logging.getLogger(__name__)

USERNAME_LENGTH = 8


class Command(BaseCommand):
    args = ''
    help = 'Make dummy photographers'

    def add_arguments(self, parser):
        parser.add_argument('event_slug', type=str)
        parser.add_argument('num_dummies', default=3, type=int)

    def handle(self, *args, **options):
        event = Event.objects.get(slug=options['event_slug'])

        for i in range(options['num_dummies']):
            username = ''.join(choice('pltkgb') for i in range(USERNAME_LENGTH))
            user, unused = User.get_or_create_dummy(username=username)
            photographer, created = Photographer.get_or_create_dummy(user=user, event=event)
            log_get_or_create(logger, photographer, created)
