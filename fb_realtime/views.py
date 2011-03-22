from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden

FACEBOOK_APP_ID = settings.FACEBOOK_APP_ID
FACEBOOK_API_KEY = settings.FACEBOOK_API_KEY
FACEBOOK_SECRET_KEY = settings.FACEBOOK_SECRET_KEY

FACEBOOK_REALTIME_VERIFY_TOKEN = settings.FACEBOOK_REALTIME_VERIFY_TOKEN

# Find a JSON parser
try:
    import json
    _parse_json = lambda s: json.loads(s)
except ImportError:
    try:
        import simplejson
        _parse_json = lambda s: simplejson.loads(s)
    except ImportError:
        # For Google AppEngine
        from django.utils import simplejson
        _parse_json = lambda s: simplejson.loads(s)

def callback_handler(request):
    if request.method == 'GET':
        try:
           if request.GET['hub_mode'] == 'subscribe' and \
              request.GET['hub_verify_token'] == FACEBOOK_REALTIME_VERIFY_TOKEN:
                  return HttpResponse(request.GET['hub_challenge'])
        except Exception, e:
            # TODO: don't feed error messages back to attackers
            return HttpResponseForbidden(e)


    elif request.method == 'POST':
        updates = _parse_json(request.read())
        print updates
