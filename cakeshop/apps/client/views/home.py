from django.http import HttpResponse
from django.template import Context, loader

def showhome(request):
    t = loader.get_template('client/home.html')
    c = Context({'request':request})
    return HttpResponse(t.render(c))