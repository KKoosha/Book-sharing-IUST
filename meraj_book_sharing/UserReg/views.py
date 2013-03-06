from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.http import HttpResponse

def loginform(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse("login Done")
            # Redirect to a success page.
            #render_to_response('login.html',{'t':'if'})
        else:
            return HttpResponse("Your curently loged in")
            #render_to_response('login.html',{'t':'first else'})
            # Return a 'disabled account' error message
    else:
        #render_to_response('login.html',{'t':'second else'})
        # Return an 'invalid login' error message.# Create your views here.
        return HttpResponse("login Failed")
def index(request):
    return HttpResponse("Done")
