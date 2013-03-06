from django.http import HttpResponse, Http404
from django.utils import simplejson

def publish_issue(request):
	# Parse the API Key from the URL
	api_key = request.GET.get('api_key')
	if api_key != '1':
		raise Http404
	# Assemble the json response
    	to_json = {
        	"status": "OK"
    	}
	return HttpResponse(simplejson.dumps(to_json), status=201,  content_type='application/json')
