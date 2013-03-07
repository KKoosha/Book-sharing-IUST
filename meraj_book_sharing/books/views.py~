# Create your views here.
from books.models import Books
from django.http import HttpResponse
from django.shortcuts import render_to_response

b1=Books(name='Linux Commands Line And Shell Scripting',author
='Richard Blum',uploader='Koosha',upload_date='1391-12-17'
,rate='0',comment='Usefull Book For People Who Wants to Learn linux',
url_pdf='home/koosha/Desktop/PDF/linuxcommand.pdf',email='-@gmail.com')
b1.save()
    
b2=Books(name='Programming and Customizing AVR',author='Dhananjay V.Gadre',uploader='Koosha',upload_date='1391-12-17'
,rate='0',comment='Fast Way to Learn AVR Programming ',
url_pdf='home/koosha/Desktop/PDF/AVR.pdf',email='-@gmail.com')
    
b2.save()
    
def download_page(request):
   # first_books()
    #Books.objects.all().delete()
    books_list=Books.objects.all()
    """b_list=[]
    b_list.append(books_list[0])
    b_list.append(books_list[1])
    b_list.append"""
    
    return render_to_response('download.html',{'books_list':books_list})
    
    
    