from django.contrib import admin

from .models import (
    Cosplayer,
    Event,
    Photographer,
)


class CosplayerAdmin(admin.ModelAdmin):
    list_display = ('event', 'display_name', 'character', 'source', 'source_type', 'is_active')
    list_filter = ('event', 'is_active')


class PhotographerAdmin(admin.ModelAdmin):
    list_display = ('event', 'display_name', 'is_official', 'is_active')
    list_filter = ('event', 'is_active', 'is_official')


admin.site.register(Cosplayer, CosplayerAdmin)
admin.site.register(Event)
admin.site.register(Photographer, PhotographerAdmin)
