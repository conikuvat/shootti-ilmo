from django.conf.urls import include, url

from django.contrib import admin

import feedback.urls
import kompassi_oauth2.urls

from .views import (
    shoottikala_frontpage_view,
    shoottikala_event_view,
    shoottikala_cosplayer_view,
    shoottikala_photographer_view,
    shoottikala_send_message_view,
)


admin.autodiscover()

urlpatterns = [
    url(
        r'^$',
        shoottikala_frontpage_view,
        name='shoottikala_frontpage_view'
    ),

    url(
        r'^events/(?P<event_slug>[a-z0-9-]+)/?$',
        shoottikala_event_view,
        name='shoottikala_event_view'
    ),

    url(
        r'^events/(?P<event_slug>[a-z0-9-]+)/cosplayers/(?P<posting_id>\d+)/?$',
        shoottikala_cosplayer_view,
        name='shoottikala_cosplayer_view'
    ),

    url(
        r'^events/(?P<event_slug>[a-z0-9-]+)/cosplayers/new/?$',
        shoottikala_cosplayer_view,
        name='shoottikala_cosplayer_create_view'
    ),

    url(
        r'^events/(?P<event_slug>[a-z0-9-]+)/photographers/(?P<posting_id>\d+)/?$',
        shoottikala_photographer_view,
        name='shoottikala_photographer_view'
    ),

    url(
        r'^events/(?P<event_slug>[a-z0-9-]+)/photographers/new/?$',
        shoottikala_photographer_view,
        name='shoottikala_photographer_create_view'
    ),

    url(
        r'^events/(?P<event_slug>[a-z0-9-]+)/message/(?P<photographer_id>\d+)/(?P<cosplayer_id>\d+)/?$',
        shoottikala_send_message_view,
        name='shoottikala_send_message_view'
    ),

    url(r'', include(kompassi_oauth2.urls)),
    url(r'', include(feedback.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
