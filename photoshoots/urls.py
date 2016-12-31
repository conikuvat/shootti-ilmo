from django.conf.urls import include, url

from django.contrib import admin

import kompassi_oauth2.urls

from .views import (
    photoshoots_frontpage_view,
    photoshoots_event_view,
    photoshoots_cosplayer_view,
    photoshoots_photographer_view,
    photoshoots_conversation_view,
)


admin.autodiscover()

urlpatterns = [
    url(
        r'^$',
        photoshoots_frontpage_view,
        name='photoshoots_frontpage_view'
    ),

    url(
        r'^events/(?P<event_slug>[a-z0-9-]+)/?$',
        photoshoots_event_view,
        name='photoshoots_event_view'
    ),

    url(
        r'^events/(?P<event_slug>[a-z0-9-]+)/cosplayers/(?P<cosplayer_id>\d+)/?$',
        photoshoots_cosplayer_view,
        name='photoshoots_cosplayer_view'
    ),

    url(
        r'^events/(?P<event_slug>[a-z0-9-]+)/cosplayers/new/?$',
        photoshoots_cosplayer_view,
        name='photoshoots_cosplayer_create_view'
    ),

    url(
        r'^events/(?P<event_slug>[a-z0-9-]+)/photographers/(?P<photographer_id>\d+)/?$',
        photoshoots_photographer_view,
        name='photoshoots_photographer_view'
    ),

    url(
        r'^events/(?P<event_slug>[a-z0-9-]+)/photographers/new/?$',
        photoshoots_photographer_view,
        name='photoshoots_photographer_create_view'
    ),

    url(
        r'^events/(?P<event_slug>[a-z0-9-]+)/conversations/(?P<conversation_id>\d+)/?$',
        photoshoots_conversation_view,
        name='photoshoots_conversation_view'
    ),

    url(r'', include(kompassi_oauth2.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
