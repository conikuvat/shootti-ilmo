from django.contrib import admin

from .models import (
    Cosplayer,
    Event,
    Photographer,
)


admin.site.register(Cosplayer)
admin.site.register(Event)
admin.site.register(Photographer)
