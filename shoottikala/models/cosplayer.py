from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth import get_user_model

from ..privileges import AccessControlMixin


SOURCE_TYPE_CHOICES = [
    ('anime', 'Anime'),
    ('other_anim', 'Muu animaatiosarja'),
    ('manga', 'Manga'),
    ('other_comic', 'Muu sarjakuva'),
    ('movie', 'Elokuva'),
    ('series', 'TV-sarja'),
    ('game', 'Videopeli'),
    ('original', 'Originaalihahmo'),
    ('other', 'Muu'),
]


class Cosplayer(AccessControlMixin, models.Model):
    event = models.ForeignKey('shoottikala.Event')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    is_active = models.BooleanField(default=True)

    display_name = models.CharField(
        max_length=255,
        verbose_name='Näyttönimi',
        help_text=(
            'Millä nimellä haluat esittäytyä valokuvaajille? Esim. nimimerkkisi, etunimesi, '
            'cosplayryhmäsi nimi tai sen jäsenten nimimerkit tai etunimet. Huomaathan, että '
            'tätä kenttää ei ole tarkoitettu hahmon nimelle vaan omallesi.'
        ),
    )

    introduction = models.TextField(
        verbose_name='Esittelyteksti',
        help_text='Esittele itsesi tai ryhmäsi muutamalla lauseella valokuvaajille ja kerro cosplayharrastuksestasi.',
    )

    source = models.CharField(
        max_length=255,
        verbose_name='Lähdeteos',
        blank=True,
        help_text=(
            'Mistä teoksesta hahmosi tai hahmonne ovat peräisin? Esim. animesarjan, elokuvan '
            'tai tietokonepelin nimi.'
        ),
    )

    source_type = models.CharField(
        max_length=max(len(key) for (key, val) in SOURCE_TYPE_CHOICES),
        verbose_name='Lähdeteoksen tyyppi',
        choices=SOURCE_TYPE_CHOICES,
    )

    character = models.CharField(
        max_length=255,
        verbose_name='Hahmon tai hahmojen nimet',
    )

    what_kinda_photos = models.TextField(
        verbose_name='Millaisia kuvia haluat asustasi?',
        help_text=(
            'Jos sinulla on jo tässä vaiheessa ajatuksia siitä, millaisia kuvia haluat – esimerkiksi taustojen, '
            'kuvakulmien tai visuaalisen tyylin suhteen – kerro niistä tässä.'
        ),
        blank=True,
    )

    reference_links = models.TextField(
        verbose_name='Referenssikuvalinkit',
        help_text='Mikäli sinulla on Internetissä referenssikuvia hahmostasi, syötä tähän niiden linkit, yksi per rivi (pelkkä osoite, https://…).',
        blank=True,
    )

    wip_links = models.TextField(
        verbose_name='WIP-kuvalinkit',
        help_text='Mikäli sinulla on Internetissä kuvia asustasi keskeneräisenä tai valmiina, syötä tähän niiden linkit, yksi per rivi (pelkkä osoite, https://…).',
        blank=True,
    )

    social_media_links = models.TextField(
        blank=True,
        verbose_name='Sosiaalisen median linkit',
        help_text='Jos sinulla on cosplay-profiili esim. Facebookissa tai Twitterissä, syötä niiden osoitteet tähän, yksi per rivi (pelkkä osoite, https://…).',
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))

    def __str__(self):
        return self.display_name

    def get_absolute_url(self):
        return reverse('shoottikala_cosplayer_view', kwargs=dict(
            event_slug=self.event.slug,
            posting_id=self.id,
        ))

    def build_absolute_uri(self, request):
        return request.build_absolute_uri(self.get_absolute_url())

    def user_can_view(self, user):
        from .photographer import Photographer

        return (
            user.is_superuser or
            self.user == user or
            Photographer.objects.filter(event=self.event, user=self.user).exists()
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
                source_type='anime',
                character='Dummy',
            ),
        )
