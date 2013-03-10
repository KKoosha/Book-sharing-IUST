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
            request.session['user'] = user
            return render_to_response('User.html',{ 'name' : request.session['user'].username })
           
        else:
            return HttpResponse("Your curently logged in")
        
    else:
        return HttpResponse("login Failed\nCheck your Username & Password, They're case-sensitive")

def logout_view(request):
    logout(request)
    try:
        del request.session['user']
    except KeyError:
        pass
    return render_to_response('loginform.html', {'logout':"You've successfully logged out"})
    
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
            return render_to_response('loginform.html', {'logout':"Your account has been created successfully!"})
        else:
            return render_to_response('loginform.html', {'logout':"Same account already exist"})
    else:
        return render_to_response('loginform.html', {'logout':"password or email confirmation doesn't match"})
