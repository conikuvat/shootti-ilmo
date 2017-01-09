from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from ..models import Event, Photographer, Cosplayer, Conversation
from ..forms import PhotographerForm, CosplayerForm, MessageForm
from ..utils import initialize_form


@login_required
def shoottikala_conversation_view(request, event_slug, photographer_id, cosplayer_id):
    event = get_object_or_404(Event, slug=event_slug)
    photographer = get_object_or_404(Photographer, event=event, id=int(photographer_id))
    cosplayer = get_object_or_404(Cosplayer, event=event, id=int(cosplayer_id))

    try:
        conversation = Conversation.objects.get(event=event, photographer=photographer, cosplayer=cosplayer)
    except Conversation.DoesNotExist:
        conversation = Conversation(
            event=event,
            photographer=photographer,
            cosplayer=cosplayer,
            initiated_by=request.user,
        )

    conversation.check_privileges(request.user)

    photographer_form = PhotographerForm(instance=photographer)
    cosplayer_form = CosplayerForm(instance=cosplayer)
    other_cosplayers_of_same_user = Cosplayer.objects.filter(event=event, user=request.user).exclude(id=cosplayer.id)
    message_form = initialize_form(MessageForm, request)

    vars = dict(
        conversation=conversation,
        cosplayer=cosplayer,
        event=event,
        other_cosplayers_of_same_user=other_cosplayers_of_same_user,
        photographer=photographer,
        photographer_form=photographer_form,
        cosplayer_form=cosplayer_form,
        message_form=message_form,
    )

    return render(request, 'shoottikala_conversation_view.jade', vars)
