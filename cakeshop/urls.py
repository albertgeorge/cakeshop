from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponsePermanentRedirect
from django.conf import settings 

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    'cakeshop.apps',
    url(r'^admin/?$',lambda request: HttpResponsePermanentRedirect('/adminlogin/')),
    url(r'^adminlogin/?$', 'admin.views.authenticate.loginuser', {'next_page': '/adminhome/'}),   
    url(r'^logout/?$', 'admin.views.authenticate.logoutuser'),
    url(r'^adminhome/?$', 'admin.views.authenticate.showadminhome'),
    url(r'^categories/?$', 'admin.views.categories.get_categories'),
    url(r'^addcategory/?$', 'admin.views.categories.add_category'),
    url(r'^showitem/?$', 'admin.views.items.show_item'),
    url(r'^addedititem/?$', 'admin.views.items.add_edit_item'),
)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))