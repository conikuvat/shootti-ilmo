from django.shortcuts import get_object_or_404, render

from ..models import Event


def photoshoots_event_view(request, event_slug):
    event = Event.objects.get(slug=event_slug)

    vars = dict(
        event=event,
    )

    return render(request, 'photoshoots_event_view.jade', vars)
