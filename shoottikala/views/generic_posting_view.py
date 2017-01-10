from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from kompassi_oauth2.forms import UserForm

from ..models import Event
from ..utils import initialize_form


def make_posting_view(
    PostingClass,
    PostingFormClass,
    create_posting_title,
    edit_posting_title,
    read_only_title,
    footer_message,
):
    @login_required
    def shoottikala_posting_view(
        request,
        event_slug,
        posting_id=None,
    ):
        event = get_object_or_404(Event, slug=event_slug)

        if posting_id is not None:
            posting = get_object_or_404(PostingClass, id=int(posting_id))
            posting.check_read_privileges(request.user)
        else:
            posting = PostingClass(event=event, user=request.user, display_name=request.user.display_name)

        user_form = UserForm(instance=request.user)

        posting_form = initialize_form(PostingFormClass, request, instance=posting)

        if request.method == 'POST':
            posting.check_write_privileges(request.user)

            if posting_form.is_valid():
                posting_form.save()

                messages.success(request, 'Ilmoitus on tallennettu.')
                return redirect('shoottikala_event_view', event.slug)
            else:
                messages.error(request, 'Ole hyvä ja tarkista lomake.')

        vars = dict(
            can_edit=posting.user == request.user,
            event=event,
            posting_form=posting_form,
            posting=posting,
            user_form=user_form,
            create_posting_title=create_posting_title,
            edit_posting_title=edit_posting_title,
            footer_message=footer_message,
            read_only_title=read_only_title,
        )

        return render(request, 'shoottikala_posting_view.jade', vars)
    return shoottikala_posting_view
