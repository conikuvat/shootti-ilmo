from django.conf import settings


def photoshoots_context(request):
    return dict(
        settings=settings,
    )
