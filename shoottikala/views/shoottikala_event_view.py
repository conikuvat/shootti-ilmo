from pprint import pprint

from django.shortcuts import get_object_or_404, render

from ..forms import PhotographerForm
from ..models import Event, Cosplayer, Photographer


def shoottikala_event_view(request, event_slug):
    event = Event.objects.get(slug=event_slug)
    is_authenticated = request.user.is_authenticated()

    if is_authenticated:
        photographer = Photographer.objects.filter(event=event, user=request.user).first()
        if photographer:
            photographer_form = PhotographerForm(instance=photographer)
        else:
            photographer_form = None

        own_cosplayers = Cosplayer.objects.filter(event=event, user=request.user)
        cosplayers_looking = Cosplayer.objects.filter(event=event, is_active=True).exclude(user=request.user)
    else:
        photographer = None
        photographer_form = None
        own_cosplayers = Cosplayer.objects.none()
        cosplayers_looking = Cosplayer.objects.filter(event=event, is_active=True)

    is_cosplayer = own_cosplayers.exists()

    vars = dict(
        cosplayers_looking=cosplayers_looking,
        event=event,
        is_cosplayer=is_cosplayer,
        own_cosplayers=own_cosplayers,
        photographer_form=photographer_form,
        photographer=photographer,
        show_cosplayer_fragment=event.is_active and is_cosplayer,
        show_inactive_fragment=not event.is_active,
        show_login_fragment=event.is_active and not is_authenticated,
        show_photographer_fragment=event.is_active and photographer,
        show_welcome_fragment=event.is_active and is_authenticated and not (is_cosplayer or photographer),
    )

    pprint(vars)

    return render(request, 'shoottikala_event_view.jade', vars)
