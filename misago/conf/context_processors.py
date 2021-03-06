import json

from django.contrib.staticfiles.templatetags.staticfiles import static
from django.urls import reverse

from misago.conf import settings

from .gateway import db_settings, dj_settings  # noqa


BLANK_AVATAR_URL = static(settings.MISAGO_BLANK_AVATAR)


def settings(request):
    return {
        'DEBUG': dj_settings.DEBUG,
        'misago_settings': db_settings,

        'BLANK_AVATAR_URL': BLANK_AVATAR_URL,

        'THREADS_ON_INDEX': dj_settings.MISAGO_THREADS_ON_INDEX,

        'LOGIN_REDIRECT_URL': dj_settings.LOGIN_REDIRECT_URL,
        'LOGIN_URL': dj_settings.LOGIN_URL,
        'LOGOUT_URL': dj_settings.LOGOUT_URL,
    }


def preload_settings_json(request):
    preloaded_settings = db_settings.get_public_settings()

    preloaded_settings.update({
        'LOGIN_API_URL': dj_settings.MISAGO_LOGIN_API_URL,

        'LOGIN_REDIRECT_URL': reverse(dj_settings.LOGIN_REDIRECT_URL),
        'LOGIN_URL': reverse(dj_settings.LOGIN_URL),

        'LOGOUT_URL': reverse(dj_settings.LOGOUT_URL),
    })

    request.frontend_context.update({
        'SETTINGS': preloaded_settings,

        'MISAGO_PATH': reverse('misago:index'),

        'BLANK_AVATAR_URL': BLANK_AVATAR_URL,
        'STATIC_URL': dj_settings.STATIC_URL,

        'CSRF_COOKIE_NAME': dj_settings.CSRF_COOKIE_NAME,

        'THREADS_ON_INDEX': dj_settings.MISAGO_THREADS_ON_INDEX,
    })

    return {}
