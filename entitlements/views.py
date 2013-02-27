# Create your views here.
from django.http import HttpResponse
from entitlements.models import Entitlement

def get_entitlements(request):
	# currently we're just returning a particular user ID
	# TODO: filter dynamically based on session ID
	output = Entitlement.objects.filter(user=2)
	# TODO: Change this to be expected JSON response - could start with displaying fields if necessary
	return HttpResponse(output)
