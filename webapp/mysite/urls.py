from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mysite.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'login/', 'UserReg.views.loginform'),
    url(r'^logout/', 'UserReg.views.logout_view'),
    url(r'signup/', 'UserReg.views.signup'),
    url(r'^download/','books.views.download_page'),
    url(r'^contact/','books.views.contact'),
    url(r'^search-form/$', 'books.views.search_form'),
    url(r'^search/$', 'books.views.search'),
    url(r'^upload/$', 'upload_app.views.list')
    #url(r'^login/' , 'mysite.templates.login.html'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
