from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ShoottikalaAppConfig(AppConfig):
    name = 'shoottikala'
    verbose_name = _('photoshoot signup')

    def ready(self):
        from . import event_log_entry_types  # noqa
        from . import handlers  # noqa
