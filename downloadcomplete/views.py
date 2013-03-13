from django.http import HttpResponse, Http404
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

@csrf_exempt

def download_complete(request):
        # Parse the API Key from the URL
        api_key = request.GET.get('api_key')
        if api_key != settings.API_KEY:
                raise Http404
        # Assemble the json response
        to_json = {
                "status": "OK"
        }
        return HttpResponse(simplejson.dumps(to_json), status=201,  content_type='application/json')

