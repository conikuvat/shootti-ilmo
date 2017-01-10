from .exceptions import AccessDenied


class AccessControlMixin(object):
    def user_can_edit(self, user):
        return (user.is_superuser or self.user == user)

    def check_privileges(self, user):
        if not self.user_can_edit(user):
            raise AccessDenied()
