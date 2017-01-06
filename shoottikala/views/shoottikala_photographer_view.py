from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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

    initial = dict(
        display_name=request.user.display_name,
    )

    photographer_form = initialize_form(PhotographerForm, request, instance=photographer, initial=initial)

    if request.method == 'POST':
        if photographer_form.is_valid():
            photographer_form.save()

            messages.success(request, 'Valokuvaajan tiedot tallennettiin.')
            return redirect('shoottikala_event_view', event.slug)
        else:
            messages.error(request, 'Ole hyvä ja tarkista lomake.')

    vars = dict(
        can_edit=True,  # XXX
        event=event,
        photographer_form=photographer_form,
        photographer=photographer,
        user_form=user_form,
    )

    return render(request, 'shoottikala_photographer_view.jade', vars)
