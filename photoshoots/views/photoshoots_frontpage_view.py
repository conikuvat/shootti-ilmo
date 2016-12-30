from django.shortcuts import render

from ..models import Event


def photoshoots_frontpage_view(request):
    events = Event.objects.all()

    vars = dict(
        events=events,
    )

    return render(request, 'photoshoots_frontpage_view.jade', vars)
