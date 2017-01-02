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


def check_same_user(self, user):
    '''
    Allow same user or superuser, otherwise raise AccessDenied.

    Usage:

    class MyModel(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL)

        from shoottikala.utils import check_same_user as check_privileges

    def my_view(request, my_model_id):
        my_model = get_object_or_404(MyModel, id=my_model_id)
        my_model.check_privileges(user)
    '''
    if not (user.is_superuser or self.user == user):
        raise AccessDenied()


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
