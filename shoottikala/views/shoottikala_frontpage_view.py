from django.shortcuts import render

from ..models import Event


def shoottikala_frontpage_view(request):
    events = Event.get_active_events()

    vars = dict(
        events=events,
    )

    return render(request, 'shoottikala_frontpage_view.jade', vars)
