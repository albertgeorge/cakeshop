from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import json
from cakeshop.services.categoryservices import CategoryService
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

def itemlist(request, category_id=0):
    item_services = ItemService()
    items = item_services.getitemsofcategoryid(category_id)
        
    page = 1
    query = request.GET.get('page')
    if query is not None:
        page = query
    
    paged_items = _get_paged_items(items['data']['items'], page, 2)
        
    return render_to_response('admin/itemlist.html',{'items':paged_items}, context_instance = RequestContext(request))

def get_data_for_adminhome(request):
    cat_services = CategoryService()
    categories = cat_services.get_categories()
    return render_to_response('admin/adminhome.html',{'categories':categories}, context_instance = RequestContext(request))

def _get_paged_items(items, page_number, number_of_items):
    paginator = Paginator(items,number_of_items)
            
    try:
        paged_items = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paged_items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paged_items = paginator.page(paginator.num_pages)
        
    return paged_items
    