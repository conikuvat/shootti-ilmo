from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

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

    class Meta:
        unique_together = [
            ('event', 'user'),
        ]
