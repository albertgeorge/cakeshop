from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
import json
from cakeshop.services.itemservices import ItemService

def show_item(request,item_id):  
    item_service = ItemService()
    item = item_service.getitem(item_id)  
    return render_to_response('admin/item.html', {'item':item['data']['item']}, context_instance = RequestContext(request))

def add_edit_item(request):
    name = request.POST.get('iteminputbox')
    category = request.POST.get('categorycombobox')
    desc = request.POST.get('desctextarea')
    files = request.FILES
    
    item_service = ItemService()
    result = item_service.saveitem(item_name=name, item_category=category, item_description=desc, files=files)
    return HttpResponse(json.dumps(result))

def new_item(request):    
    return render_to_response('admin/newitem.html', context_instance = RequestContext(request))