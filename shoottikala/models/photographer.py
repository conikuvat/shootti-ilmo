from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.urlresolvers import reverse

from ..privileges import AccessControlMixin


class Photographer(AccessControlMixin, models.Model):
    event = models.ForeignKey('shoottikala.Event')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    display_name = models.CharField(
        max_length=255,
        verbose_name='Näyttönimi',
        help_text='Millä nimellä haluat esittäytyä cossaajille?',
    )
    introduction = models.TextField(
        # verbose_name=_('Introduction'),
        # help_text=_('Please introduce yourself in a few sentences.'),
        verbose_name='Esittely',
        help_text='Kerro itsestäsi valokuvaajana muutamalla lauseella.',
    )

    portfolio_links = models.TextField(
        blank=True,
        verbose_name='Portfolio- ja gallerialinkit',
        help_text='Jos sinulla on Internetissä portfolio tai kuvagallerioita, syötä niiden osoitteet tähän, yksi per rivi (pelkkä osoite, https://…).',
    )

    social_media_links = models.TextField(
        blank=True,
        verbose_name='Sosiaalisen median linkit',
        help_text='Jos sinulla on kuvaajaprofiili esim. Facebookissa tai Twitterissä, syötä niiden osoitteet tähän, yksi per rivi (pelkkä osoite, https://…).',
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))

    def __str__(self):
        return self.display_name

    def get_absolute_url(self):
        return reverse('shoottikala_photographer_view', kwargs=dict(
            event_slug=self.event.slug,
            photographer_id=self.id,
        ))

    def build_absolute_uri(self, request):
        return request.build_absolute_uri(self.get_absolute_url())

    def user_can_view(self, user):
        from .cosplayer import Cosplayer

        return (
            user.is_superuser or
            self.user == user or
            Cosplayer.objects.filter(event=self.event, user=self.user).exists()
        )

    @classmethod
    def get_or_create_dummy(cls, event=None, user=None):
        if event is None:
            from .event import Event
            event, unused = Event.get_or_create_dummy()

        if user is None:
            User = get_user_model()
            user, unused = User.get_or_create_dummy()

        return cls.objects.get_or_create(
            event=event,
            user=user,
            defaults=dict(
                display_name=user.display_name,
                introduction='Such dummy, wow',
            ),
        )

    class Meta:
        unique_together = [
            ('event', 'user'),
        ]
