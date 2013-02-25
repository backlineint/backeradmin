# Create your views here.
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse

def handler(request):
    session_token = request.session._session_key
    if request.user.is_authenticated():
        return HttpResponse('%s is logged in' % session_token)
        #return HttpResponseRedirect("magplus://myaccountview/login%s" % session_token)
    else:
        return HttpResponse('%s is not logged in' % session_token)
