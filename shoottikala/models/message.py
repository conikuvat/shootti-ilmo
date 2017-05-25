from django.db import models


INITIATED_BY_CHOICES = [
    ('c', 'Cosplayer'),
    ('p', 'Photographer'),
]


class Message(models.Model):
    """
    Stores a record that a message has been sent. Message contents are not saved.
    """

    cosplayer = models.ForeignKey('shoottikala.Cosplayer')
    photographer = models.ForeignKey('shoottikala.Photographer')
    initiated_by = models.CharField(
        max_length=max(len(key) for (key, label) in INITIATED_BY_CHOICES),
        choices=INITIATED_BY_CHOICES,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{sender} -> {receiver}'.format(
            sender=self.sender,
            receiver=self.receiver,
        )

    @property
    def sender(self):
        return self.cosplayer if self.initiated_by == 'c' else self.photographer

    @property
    def receiver(self):
        return self.photographer if self.initiated_by == 'c' else self.cosplayer

    def admin_get_event(self):
        return self.cosplayer.event
    admin_get_event.short_description = 'Event'
    admin_get_event.admin_order_field = 'cosplayer__event'
