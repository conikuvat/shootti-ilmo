from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    nick = models.CharField(
        blank=True,
        max_length=1023,
        verbose_name='Nick',
    )

    phone = models.CharField(
        blank=True,
        max_length=255,
        verbose_name='Puhelinnumero',
    )

    display_name = models.CharField(
        max_length=2047,
        blank=True,
    )
