from django.db import models
from django.utils.translation import ugettext_lazy as _


class Event(models.Model):
    slug = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_('slug'),
    )

    name = models.CharField(max_length=63, verbose_name=_('name'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))
