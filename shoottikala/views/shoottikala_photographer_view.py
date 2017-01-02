from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from kompassi_oauth2.forms import UserForm

from ..models import Event, Photographer
from ..forms import PhotographerForm
from ..utils import initialize_form


@login_required
def shoottikala_photographer_view(request, event_slug, photographer_id=None):
    event = get_object_or_404(Event, slug=event_slug)

    if photographer_id is not None:
        photographer = get_object_or_404(id=int(photographer_id))
    else:
        photographer = Photographer(event=event, user=request.user)

    photographer.check_privileges(request.user)

    user_form = UserForm(instance=request.user)
    photographer_form = initialize_form(PhotographerForm, request, instance=photographer)

    vars = dict(
        can_edit=True,  # XXX
        event=event,
        photographer_form=photographer_form,
        photographer=photographer,
        user_form=user_form,
    )

    return render(request, 'shoottikala_photographer_view.jade', vars)
