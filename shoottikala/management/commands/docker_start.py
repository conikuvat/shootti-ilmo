# encoding: utf-8

import logging

from django.conf import settings
from django.db import ProgrammingError
from django.core.management import call_command
from django.core.management.base import BaseCommand


logger = logging.getLogger('kompassi')


class Command(BaseCommand):
    args = ''
    help = 'Docker development environment entry point'

    def handle(self, *args, **options):
        from shoottikala.models import Event

        test = settings.DEBUG

        if not test:
            raise ValueError('Should run with DEBUG=true')

        try:
            Event.objects.first()
        except ProgrammingError:
            call_command('setup')

        call_command('runserver', '0.0.0.0:8000')
