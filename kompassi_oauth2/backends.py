from django.conf import settings

from .models import User


def user_attrs_from_kompassi(kompassi_user):
    return dict((django_key, accessor_func(kompassi_user)) for (django_key, accessor_func) in [
        # ('username', lambda u: u['username']),
        ('email', lambda u: u['email']),
        ('first_name', lambda u: u['first_name']),
        ('last_name', lambda u: u['surname']),
        ('nick', lambda u: u['nick']),
        ('display_name', lambda u: u['display_name']),
        ('is_superuser', lambda u: settings.KOMPASSI_ADMIN_GROUP in u['groups']),
        ('is_staff', lambda u: settings.KOMPASSI_ADMIN_GROUP in u['groups']),
    ])


class KompassiOAuth2AuthenticationBackend(object):
    def authenticate(self, oauth2_session=None, **kwargs):
        if oauth2_session is None:
            # Not ours (password login)
            return None

        response = oauth2_session.get(settings.KOMPASSI_API_V2_USER_INFO_URL)
        response.raise_for_status()
        kompassi_user = response.json()
        user_attrs = user_attrs_from_kompassi(kompassi_user)

        user, created = User.objects.update_or_create(username=kompassi_user['username'], defaults=user_attrs)

        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesDotExist:
            return None
