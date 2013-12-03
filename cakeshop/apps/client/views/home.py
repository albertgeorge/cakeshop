from django.http import HttpResponse
from django.template import Context, loader
from django.template import RequestContext
from django.shortcuts import render_to_response

def showhome(request):
    t = loader.get_template('client/home.html')
    categories = [{'id':1,'name':'wedding cakes'},{'id':1,'name':'fondant cakes'},{'id':1,'name':'cream cakes'},{'id':1,'name':'cupcakes'},{'id':1,'name':'sugar-free cakes'},{'id':1,'name':'cheese cakes'},{'id':1,'name':'cookies'},{'id':1,'name':'other desserts'}]
    images = [{'img':'/static/images/client/wedding-cupcakes-large.jpg','active':True},{'img':'/media/IMG_6616.JPG','active':False}]
    c = Context({'request':request,'categories':categories,'images':images})
    return HttpResponse(t.render(c))

def about(request):
    t = loader.get_template('client/about.html')
    c = Context({'request':request})
    return HttpResponse(t.render(c))

def get_new_items(request):
    items = [{'name':'cake 01','description':'test desc for this cake','image':''},{'name':'cake 02','description':'test desc for this cake','image':''},{'name':'cake 03','description':'test desc for this cake','image':''}]
    return render_to_response('client/itemlist.html',{'items':items}, context_instance = RequestContext(request))