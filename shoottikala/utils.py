from django.utils.timezone import now

from crispy_forms.helper import FormHelper

from .exceptions import AccessDenied


def log_get_or_create(logger, obj, created):
    logger.info('{kind} {name} {what_done}'.format(
        kind=obj.__class__.__name__,
        name=str(obj),
        what_done='created' if created else 'already exists',
    ))


def make_horizontal_form_helper(helper):
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-md-3'
    helper.field_class = 'col-md-9'
    return helper


def horizontal_form_helper():
    return make_horizontal_form_helper(FormHelper())


def is_within_period(period_start, period_end, t=None):
    if t is None:
        t = now()

    return period_start and period_start <= t and \
        not (period_end and period_end <= t)


def initialize_form(FormClass, request, **kwargs):
    if request.method == 'POST':
        form = FormClass(request.POST, **kwargs)
    else:
        form = FormClass(**kwargs)

    return form
