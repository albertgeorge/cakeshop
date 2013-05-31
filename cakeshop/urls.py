from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponsePermanentRedirect

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    'cakeshop.apps',
    url(r'^admin/?$',lambda request: HttpResponsePermanentRedirect('/adminlogin/')),
    url(r'^adminlogin/?$', 'admin.views.loginuser', {'next_page': '/adminhome/'}),   
    url(r'^logout/?$', 'admin.views.logoutuser'),
    url(r'^adminhome/?$', 'admin.views.showadminhome'), 
)

urlpatterns += staticfiles_urlpatterns()