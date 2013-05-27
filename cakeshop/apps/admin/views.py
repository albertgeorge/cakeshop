from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.template import RequestContext

def loginuser(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if (user is not None) and user.is_active:                
                login(request, user)
                return render_to_response('adminhome.html', context_instance = RequestContext(request))
        
    if request.user.is_authenticated():
        return render_to_response('adminlogin.html', {'state' : ''}, context_instance = RequestContext(request))
    
    return render_to_response('adminlogin.html', {'state' : 'Incorrect username/password'}, context_instance = RequestContext(request)) 
