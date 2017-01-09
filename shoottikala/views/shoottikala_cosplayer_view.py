from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from kompassi_oauth2.forms import UserForm

from ..models import Event, Cosplayer
from ..forms import CosplayerForm
from ..utils import initialize_form


@login_required
def shoottikala_cosplayer_view(request, event_slug, cosplayer_id=None):
    event = get_object_or_404(Event, slug=event_slug)

    if cosplayer_id is not None:
        cosplayer = get_object_or_404(Cosplayer, id=int(cosplayer_id))
    else:
        cosplayer = Cosplayer(event=event, user=request.user, display_name=request.user.display_name)

    cosplayer.check_read_privileges(request.user)

    user_form = UserForm(instance=request.user)

    cosplayer_form = initialize_form(CosplayerForm, request, instance=cosplayer)

    if request.method == 'POST':
        cosplayer.check_write_privileges(request.user)

        if cosplayer_form.is_valid():
            cosplayer_form.save()

            messages.success(request, 'Cossaajan tiedot tallennettiin.')
            return redirect('shoottikala_event_view', event.slug)
        else:
            messages.error(request, 'Ole hyvä ja tarkista lomake.')

    vars = dict(
        can_edit=cosplayer.user_can_edit(request.user),
        event=event,
        cosplayer_form=cosplayer_form,
        cosplayer=cosplayer,
        user_form=user_form,
    )

    return render(request, 'shoottikala_cosplayer_view.jade', vars)
