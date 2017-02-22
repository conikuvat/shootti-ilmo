from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class FeedbackAppConfig(AppConfig):
    name = 'feedback'
    verbose_name = _('feedback')

    def ready(self):
        from . import event_log_entry_types  # noqa
        from . import handlers  # noqa
