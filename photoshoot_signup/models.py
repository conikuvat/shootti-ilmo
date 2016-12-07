from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Event(models.Model):
    slug = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_('slug'),
    )

    name = models.CharField(max_length=63, verbose_name=_('name'))


class Photographer(models.Model):
    event = models.ForeignKey(Event)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)


class PhotoModel(models.Model):
    event = models.ForeignKey(Event)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)