# Create your views here.
from django.contrib import auth
from django.contrib.auth.views import login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

def custom_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/myaccount/")
    else:
        return login(request)

def handler(request):
    session_token = request.session._session_key
    if request.user.is_authenticated():
        response = HttpResponse("", status=302)
        response['Location'] = "magplus://myaccountview/login/%s" % session_token
        return response
    else:
        return HttpResponse('Error: session token is not valid')

def myaccount(request):
    if request.user.is_authenticated():
        return render(request, 'myaccount/myaccount.html')
    else:
        return login(request)

def myaccount_changed(request):
    if request.user.is_authenticated():
        return render(request, 'myaccount/myaccount_changed.html')
    else:
        return login(request)


def custom_logout(request):
    logout(request)
    #return redirect('app.home.views.home')
    response = HttpResponse("", status=302)
    response['Location'] = "magplus://myaccountview/logout/"
    return response

def close(request):
    response = HttpResponse("", status=302)
    response['Location'] = "magplus://myaccountview/close/"
    return response

def catch_all(request):
    return HttpResponse("Page does not exist.  For support contact support@paperweightmagazine.com")
