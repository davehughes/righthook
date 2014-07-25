from django.conf import settings

RIGHTHOOK_BASE_URL = getattr(settings, 'RIGHTHOOK_BASE_URL', 'webhooks')
RIGHTHOOK_REQUEST_PARAMS = getattr(settings, 'RIGHTHOOK_REQUEST_PARAMS', {
    'GET', 
    'POST', 
    'META.SERVER_NAME',
    'META.HTTP_HOST',
    'META.REQUEST_METHOD',
    'META.CONTENT_TYPE',
    'META.REMOTE_HOST',
    'META.REMOTE_ADDR',
    'META.TZ',
    })

RIGHTHOOK_MAX_BODY_SIZE = getattr(settings, 'RIGHTHOOK_MAX_BODY_SIZE', 1024)
