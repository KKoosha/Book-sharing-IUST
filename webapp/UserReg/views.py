from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.http import HttpResponse

def loginform(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render_to_response('User.html',{ 'name' : user.username })
           # return HttpResponse("login Done")
            # Redirect to a success page.
            #render_to_response('login.html',{'t':'if'})
        else:
            return HttpResponse("Your curently logged in")
            #render_to_response('login.html',{'t':'first else'})
            # Return a 'disabled account' error message
    else:
        #render_to_response('login.html',{'t':'second else'})
        # Return an 'invalid login' error message.# Create your views here.
        return HttpResponse("login Failed\nCheck your Username & Password, They're case-sensitive")

def logout_view(request):
    logout(request)
    return HttpResponse("You've successfully logged out")
    
def signup(request):
    name = request.POST['name']
    username = request.POST['username']
    password = request.POST['password']
    cpassword = request.POST['cpassword']
    email = request.POST['email']
    cemail = request.POST['cemail']
    agree = request.POST['agree']
    user = authenticate(username=username, password=password)
    if password == cpassword and email == cemail:
        if user is None:
            newuser = User.objects.create_user(username, email, password)
            newuser.save()
            return HttpResponse("your account has been created successfully!")
        else:
            return HttpResponse("Same account already exist")
    else:
        return HttpResponse("password or email confirmation doesn't match")
            
        
    
    return HttpResponse("Done")
