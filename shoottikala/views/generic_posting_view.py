from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from kompassi_oauth2.forms import UserForm

from ..models import Event
from ..utils import initialize_form
from ..exceptions import InvalidAction


def make_posting_view(
    PostingClass,
    PostingFormClass,
    view_name,
    allow_multiple_postings,
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

        if posting_id is None:
            # About to create a new posting
            if not allow_multiple_postings:
                try:
                    existing_posting = PostingClass.objects.get(event=event, user=request.user)
                except PostingClass.DoesNotExist:
                    pass
                else:
                    messages.warning(request, (
                        'Sinulla on jo ilmoitus tähän tapahtumaan. '
                        'Sinulla ei voi olla useampia tämäntyyppisiä ilmoituksia.'
                    ))
                    return redirect(view_name, event.slug, existing_posting.id)

            posting = PostingClass(event=event, user=request.user, display_name=request.user.display_name)
        else:
            posting = get_object_or_404(PostingClass, id=int(posting_id))
            posting.check_read_privileges(request.user)

        user_form = UserForm(instance=request.user)

        posting_form = initialize_form(PostingFormClass, request, instance=posting)

        if request.method == 'POST':
            posting.check_write_privileges(request.user)
            action = request.POST.get('action')

            if action == 'save':
                if posting_form.is_valid():
                    posting_form.save()

                    messages.success(request, 'Ilmoitus on tallennettu.')
                    return redirect('shoottikala_event_view', event.slug)
                else:
                    messages.error(request, 'Ole hyvä ja tarkista lomake.')
            elif action == 'hide':
                if posting.is_active:
                    posting.is_active = False
                    posting.save()
                    messages.success(request, 'Ilmoitus on nyt piilotettu.')
                else:
                    messages.error(request, 'Ilmoitus on jo piilossa.')

                return redirect('shoottikala_event_view', event.slug)
            elif action == 'restore':
                if not posting.is_active:
                    posting.is_active = True
                    posting.save()
                    messages.success(request, 'Ilmoitus on nyt palautettu.')
                else:
                    messages.error(request, 'Ilmoitus on jo näkyvissä.')

                return redirect('shoottikala_event_view', event.slug)
            else:
                raise InvalidAction(action)

        vars = dict(
            can_edit=posting.user == request.user and posting.is_active,
            can_restore=posting.user == request.user and not posting.is_active,
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
