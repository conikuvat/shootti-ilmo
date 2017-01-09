from .exceptions import AccessDenied


class AccessControlMixin(object):
    def check_privileges(self, user):
        return user.is_superuser or self.user == user
