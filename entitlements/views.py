from django.http import HttpResponse, Http404
from entitlements.models import Entitlement, Issue
from django.utils import simplejson
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from array import *

def get_entitlements(request):
	# TODO: Test for shared secret
	# Parse the API Key from the URL
	api_key = request.GET.get('api_key')
	if api_key != '1':
		raise Http404
	# Parse the session token from the URL
	session_key = request.GET.get('session_token')
	# Grab the session object for this session token and derive the username
	session = Session.objects.get(session_key=session_key)
        uid = session.get_decoded().get('_auth_user_id')
        user = User.objects.get(pk=uid)
        username =  user.username
	# Create an array to hold entitlements and then populate it
	issue_id = array('l')
	for e in Entitlement.objects.filter(user=uid):
		issue_id.append(e.issue.issue_id)
	# Assemble the json response
    	to_json = {
        	"username": str(username),
		"entitlements": issue_id.tolist()
		#"session_token": str(session_key)
    	}
	return HttpResponse(simplejson.dumps(to_json), content_type='application/json')

	# TODO - More gracefully handle errors in cases where the session_token or API token is not valid
 	# TODO - Also cases where the user has no entitlements
