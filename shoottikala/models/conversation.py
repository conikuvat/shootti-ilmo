from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Conversation(models.Model):
    event = models.ForeignKey('shoottikala.Event')
    photographer = models.ForeignKey('shoottikala.Photographer')
    cosplayer = models.ForeignKey('shoottikala.Cosplayer')

    initiated_by = models.ForeignKey(settings.AUTH_USER_MODEL)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))

    def __str__(self):
        return '{photographer} / {cosplayer}'.format(photographer=self.photographer, cosplayer=self.cosplayer)

    def check_privileges(self, user):
        # not even superusers may view conversations of other users
        return user in (self.photographer.user, self.cosplayer.user)

    class Meta:
        unique_together = [
            ('event', 'photographer', 'cosplayer'),
        ]
