import logging
from contextlib import contextmanager

from django.conf import settings
from django.core.management import call_command
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db.transaction import atomic

from ...utils import log_get_or_create


logger = logging.getLogger(__name__)


@contextmanager
def noop_context():
    yield


class Command(BaseCommand):
    args = ''
    help = 'Setup all the things'

    def handle(self, *args, **options):
        management_commands = [
            # (('kompassi_i18n', '-acv2'), dict()),
            # (('collectstatic',), dict(interactive=False)),
            (('migrate',), dict()),
        ]

        for pargs, opts in management_commands:
            print('** Running:', pargs[0])
            with (atomic() if pargs[0].startswith("setup") else noop_context()):
                call_command(*pargs, **opts)

        if settings.DEBUG:
            user, created = get_user_model().objects.get_or_create(
                username='mahti',
                defaults=dict(
                    first_name='Markku',
                    last_name='Mahtinen',
                    is_staff=True,
                    is_superuser=True,
                ),
            )

            if created:
                user.set_password('mahti')
                user.save()

            log_get_or_create(logger, user, created)