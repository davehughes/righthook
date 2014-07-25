from django import http
from righthook import appsettings, tasks


def receive_hook(request):
    # from righthook import tasks
    tasks.process_hook.delay(request.path, serialize_request(request))
    return http.HttpResponse(200)


def serialize_request(request):
    r = {}
    for key in appsettings.RIGHTHOOK_REQUEST_PARAMS:
        r[key] = access_key(request, key)
    return r


def access_key(root, key, sep='.', default=None):
    '''
    Look up a key in a potentially nested object `root` by its `sep`-separated
    path. Returns `default` if the key is not found.

    Example:
        access_key({'foo': {'bar': 1}}, 'foo.bar') -> 1
    '''
    props = key.split('.')
    props.reverse()
    while props and root:
        prop = props.pop()
        root = access(root, prop, default=default)
    return root


def access(obj, prop, default=None):
    try:
        return getattr(obj, prop)
    except AttributeError as e:
        pass

    try:
        return obj[prop]
    except (KeyError, TypeError) as e:
        pass

    return default
