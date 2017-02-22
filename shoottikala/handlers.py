from event_log.utils import log_creations, INSTANCE

from .models import Cosplayer, Photographer


log_creations(
    Cosplayer,
    cosplayer=INSTANCE,
    created_by=lambda cosplayer: cosplayer.user
)

log_creations(
    Photographer,
    photographer=INSTANCE,
    created_by=lambda photographer: photographer.user
)
