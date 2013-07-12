from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from cakeshop.services.categoryservices import CategoryService
import json

def get_categories(request):
    cat_service = CategoryService()
    cat_list = cat_service.get_categories()
    return HttpResponse(json.dumps(cat_list), mimetype='application/json') 

def add_category(request):
    category_name = request.POST['name']
    cat_service = CategoryService()
    result = cat_service.add_category(category_name)
    return HttpResponse(result) 