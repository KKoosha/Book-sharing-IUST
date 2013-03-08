from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^polls/$', 'polls.views.index'),
    #url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
    #url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
    #url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'UserReg.views.loginform'),
    url(r'^logout/', 'UserReg.views.logout_view'),
    url(r'^signup/', 'UserReg.views.signup'),
    url(r'^download/','books.views.download_page'),
    url(r'^contact/','books.views.contact'),
    url(r'^search-form/$', 'books.views.search_form'),
    url(r'^search/$', 'books.views.search'),
    url(r'^upload/$', 'upload_app.views.list')
    #url(r'^login/' , 'mysite.templates.login.html'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
