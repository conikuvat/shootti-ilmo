import logging

from django.db import models

from ..utils import log_get_or_create


logger = logging.getLogger(__name__)


class Day(models.Model):
    name = models.CharField(max_length=31)
    abbreviation = models.CharField(max_length=3)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Päivä'
        verbose_name_plural = 'Päivät'

    def __str__(self):
        return self.name

    @classmethod
    def ensure_days_exist(cls):
        for day_id, day_name, day_abbreviation in [
            (4, 'Perjantai', 'Pe'),
            (5, 'Lauantai', 'La'),
            (6, 'Sunnuntai', 'Su'),
        ]:
            day, created = cls.objects.get_or_create(id=day_id, defaults=dict(
                name=day_name,
                abbreviation=day_abbreviation
            ))
            log_get_or_create(logger, day, created)
