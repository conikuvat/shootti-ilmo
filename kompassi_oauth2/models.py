from django.contrib.auth.models import AbstractUser
from django.db import models


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

    @classmethod
    def get_or_create_dummy(cls, username='dummy'):
        first_name = username.capitalize()
        last_name = ''.join(reversed(username)).capitalize()
        display_name = '{first_name} {last_name}'.format(**locals())
        email = '{username}@example.com'.format(**locals())
        phone = '+358 555 1234'

        return cls.objects.get_or_create(
            username=username,
            defaults=dict(
                first_name=first_name,
                last_name=last_name,
                display_name=display_name,
                email=email,
                phone=phone,
            ),
        )
