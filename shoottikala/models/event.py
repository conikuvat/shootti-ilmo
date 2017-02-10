from django.db import models
from django.db.models import Q
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _

from ..utils import is_within_period


KOMPASSI_EVENT_ATTRS = [
    'slug',
    'name',
    'homepage_url',
    'headline',
]


class Event(models.Model):
    slug = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_('slug'),
    )

    name = models.CharField(max_length=63, verbose_name=_('name'))

    homepage_url = models.CharField(max_length=255, blank=True)
    headline = models.CharField(max_length=255, blank=True)
    organization_name = models.CharField(max_length=255, blank=True)
    organization_url = models.CharField(max_length=255, blank=True)

    active_from = models.DateTimeField(blank=True, null=True)
    active_until = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.name

    @property
    def is_active(self):
        return is_within_period(self.active_from, self.active_until)

    @classmethod
    def get_active_events(cls, t=None, **kwargs):
        if t is None:
            t = now()

        q = (
            # starting time is defined and it has been passed
            Q(active_from__isnull=False, active_from__lte=t) &

            # if ending time is defined, it must not yet have been passed
            ~Q(active_until__isnull=False, active_until__lte=t)
        )

        return cls.objects.filter(q)

    @classmethod
    def from_dict(cls, kompassi_event):
        '''
        Constructs an unsaved Event from a Kompassi API v2 event JSON dict.
        '''
        event = cls()
        event.update_from_dict(kompassi_event)
        return event

    def update_from_dict(self, kompassi_event):
        for attr_name in KOMPASSI_EVENT_ATTRS:
            setattr(self, attr_name, kompassi_event[attr_name])

        self.organization_name = kompassi_event['organization']['name']
        self.organization_url = kompassi_event['organization']['homepage_url']
