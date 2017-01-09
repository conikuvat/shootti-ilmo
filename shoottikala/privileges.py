from .exceptions import AccessDenied


class AccessControlMixin(object):
    def check_read_privileges(self, user):
        from .models import Cosplayer
        from .models import Photographer

        if user.is_superuser:
            return

        if not (
            Cosplayer.objects.filter(event=self.event, user=user).exists() or
            Photographer.objects.filter(event=self.event, user=user).exists()
        ):
            raise AccessDenied()

    def user_can_edit(self, user):
        return self.user == user

    def check_write_privileges(self, user):
        if not self.user_can_edit(user):
            raise AccessDenied()
