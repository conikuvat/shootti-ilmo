from django.contrib import admin

from .models import (
    Conversation,
    Cosplayer,
    Event,
    Message,
    Photographer,
)


admin.site.register(Conversation)
admin.site.register(Cosplayer)
admin.site.register(Event)
admin.site.register(Message)
admin.site.register(Photographer)
