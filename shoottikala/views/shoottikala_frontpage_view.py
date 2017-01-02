from django.shortcuts import render

from ..models import Event


def shoottikala_frontpage_view(request):
    events = Event.objects.all()

    vars = dict(
        events=events,
    )

    return render(request, 'shoottikala_frontpage_view.jade', vars)
