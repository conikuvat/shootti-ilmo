from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Cosplayer(models.Model):
    event = models.ForeignKey('photoshoots.Event')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))
