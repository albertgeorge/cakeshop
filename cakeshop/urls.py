from django.conf.urls.defaults import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('cakeshop.apps',
    url(r'/?$', 'admin.views.loginuser',name='loginuser'),
)
