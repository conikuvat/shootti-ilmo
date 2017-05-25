from django.contrib import admin

from .models import (
    Cosplayer,
    Event,
    Message,
    Photographer,
)


class CosplayerAdmin(admin.ModelAdmin):
    list_display = ('event', 'display_name', 'character', 'source', 'source_type', 'is_active')
    list_filter = ('event', 'is_active')


class PhotographerAdmin(admin.ModelAdmin):
    list_display = ('event', 'display_name', 'is_official', 'is_active')
    list_filter = ('event', 'is_active', 'is_official')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'admin_get_event', 'cosplayer', 'photographer', 'initiated_by')
    list_filter = ('cosplayer__event', 'initiated_by')
    readonly_fields = ('cosplayer', 'photographer', 'initiated_by', 'created_at')

    def has_add_permission(self, *args, **kwargs):
        return False

    def has_delete_permission(self, *args, **kwargs):
        return False


admin.site.register(Cosplayer, CosplayerAdmin)
admin.site.register(Event)
admin.site.register(Photographer, PhotographerAdmin)
admin.site.register(Message, MessageAdmin)
