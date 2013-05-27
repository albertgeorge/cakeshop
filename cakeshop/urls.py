from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    'cakeshop.apps',
    url(r'^admin/?$', 'admin.views.loginuser',name='admin_login'),    
)

urlpatterns += staticfiles_urlpatterns()