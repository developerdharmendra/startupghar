from django.conf import settings


def global_context(request):
    return {
        "SITE_NAME": settings.SITE_NAME,
    }
