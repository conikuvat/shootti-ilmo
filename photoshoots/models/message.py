from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Message(models.Model):
    conversation = models.ForeignKey('photoshoots.Conversation')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL)
    body = models.TextField()
    share_contact_details = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
