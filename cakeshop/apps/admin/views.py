from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.views import logout
from django.core.urlresolvers import reverse

def loginuser(request, next_page):
    state=''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(username=username, password=password)            
            if (user is not None) and user.is_active:                
                login(request, user)
                return HttpResponseRedirect(request.GET.get("next",next_page))
            else:
                state='Incorrect username/password'
        
    if request.user.is_authenticated():
        return HttpResponseRedirect(request.GET.get("next", next_page))    
    
    return render_to_response('adminlogin.html', {'state' : state}, context_instance = RequestContext(request)) 

@login_required    
def showadminhome(request):
    return render_to_response('adminhome.html', context_instance = RequestContext(request))

@login_required
def logoutuser(request):
    logout(request)
    return HttpResponseRedirect(reverse('cakeshop.apps.admin.views.loginuser'))