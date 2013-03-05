# Create your views here.
from django.http import HttpResponse
from entitlements.models import Entitlement, Issue
from django.utils import simplejson
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

def get_entitlements(request):
	# TODO: Test for shared secret
	# Parse the session token from the URL
	session_key = request.GET.get('session_token')
	# Grab the session object for this session token and derive the username
	session = Session.objects.get(session_key=session_key)
        uid = session.get_decoded().get('_auth_user_id')
        user = User.objects.get(pk=uid)
        username =  user.username
	# Work in progress below here
	results = Entitlement.objects.get(user=2)
	# TODO - Handle getting multiple entitlements
	#results = Entitlement.objects.filter(user=2)
	#username = results.user
	# TODO - Change this to get the right ID
	issue = results.issue
	#, user.get_full_name(), user.email
    	to_json = {
        	"username": str(username),
        	"issue": str(issue),
		"session_token": str(session_key)
    	}
	return HttpResponse(simplejson.dumps(to_json), content_type='application/json')
