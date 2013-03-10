
from books.models import Books
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from mysite.forms import ContactForm
from books import models
from books.models import Books
from upload_app.models import PDF

def contact(request):
    user=request.session['user']
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render_to_response('contact_form.html', {'form': form,'name':user.username})

def search_form(request):
    try:
        user=request.session['user']
        if user.is_authenticated() :
            return render_to_response('search_form.html',{'name' : user.username})
    except:
        return render_to_response('loginform.html', {'logout':"You must login first!"})
def search(request):
    try:
        user=request.session['user']
        if user.is_authenticated() :
            if 'q' in request.GET and request.GET['q']:
                q = request.GET['q']
                books = PDF.objects.filter(name__icontains=q)
                return render_to_response('search_results.html',
                    {'books': books, 'query': q, 'name':user.username})
            else:
                return render_to_response('search_form.html', {'error': True})
    except:
        return render_to_response('loginform.html', {'logout':"You must login first!"})


def download_page(request):
    try:
        user=request.session['user']
        if user.is_authenticated() :
            allbooks=PDF.objects.all()
            return render_to_response('download.html',{'books_list':allbooks,'name':user.username})
        else :
            return HttpResponse("you're not logged in")
    except:
        return render_to_response('loginform.html', {'logout':"You must login first!"})
    
    
