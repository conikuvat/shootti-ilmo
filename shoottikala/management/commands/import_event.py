import logging

from django.core.management.base import BaseCommand

from kompassi_oauth2.utils import get_event

from ...models import Event

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    args = ''
    help = 'Import an event from Kompassi'

    def add_arguments(self, parser):
        parser.add_argument('event_slugs', nargs='+', type=str)

    def handle(self, *args, **options):
        for event_slug in options['event_slugs']:
            logger.info('Importing event %s', event_slug)

            kompassi_event = get_event(event_slug)

            event = Event.from_dict(kompassi_event)
            event.save()
