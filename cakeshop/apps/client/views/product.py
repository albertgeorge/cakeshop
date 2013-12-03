from django.http import HttpResponse
from django.template import Context, loader

def show_products(request):
    t = loader.get_template('client/product.html')
    c = Context({'request':request})
    return HttpResponse(t.render(c))