from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


SOURCE_TYPE_CHOICES = [
    ('anime', 'Anime (japanilainen animaatiosarja tai -elokuva)'),
    ('other_anim', 'Muu animaatiosarja'),
    ('manga', 'Manga (japanilainen sarjakuva)'),
    ('other_comic', 'Muu sarjakuva'),
    ('movie', 'Elokuva'),
    ('series', 'TV-sarja'),
    ('game', 'Videopeli'),
    ('original', 'Originaalihahmo'),
    ('other', 'Muu'),
]


class Cosplayer(models.Model):
    event = models.ForeignKey('photoshoots.Event')
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

    reference_links = models.TextFields(
        verbose_name='Referenssikuvalinkit',
        help_text='Mikäli sinulla on Internetissä referenssikuvia hahmostasi, syötä tähän niiden linkit, yksi per rivi (pelkkä osoite, https://…).',
        blank=True,
    )

    wip_links = models.TextFields(
        verbose_name='WIP-kuvalinkit',
        help_text='Mikäli sinulla on Internetissä kuvia asustasi keskeneräisenä tai valmiina, syötä tähän niiden linkit, yksi per rivi (pelkkä osoite, https://…).',
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))
