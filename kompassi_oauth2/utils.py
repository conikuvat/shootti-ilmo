from django.conf import settings

import requests


def get_event(event_slug):
    url = settings.KOMPASSI_API_V2_EVENT_INFO_URL_TEMPLATE.format(
        kompassi_host=settings.KOMPASSI_HOST,
        event_slug=event_slug,
    )

    response = requests.get(url)

    return response.json()
