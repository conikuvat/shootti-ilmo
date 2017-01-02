from django.conf import settings


def shoottikala_context(request):
    return dict(
        settings=settings,
    )
