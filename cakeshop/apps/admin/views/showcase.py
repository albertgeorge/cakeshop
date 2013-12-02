from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from cakeshop.services.showcaseservices import ShowcaseService
import json

def show_showcase(request):    
    return render_to_response('admin/showcase.html',{}, context_instance = RequestContext(request))

def get_showcase_items(request):
    showcase_services = ShowcaseService()
    result = showcase_services.getselectedshowcaseitems()
    
    page = 1
    query = request.GET.get('page')
    if query is not None:
        page = query
    
    paged_items = _get_paged_items(result['data']['showcase'], page, 12)
    
    return render_to_response('admin/showcaselist.html',{'showcase':paged_items}, context_instance = RequestContext(request))

def set_showcase(request):
    item_image_ids = request.POST.get('items')
    showcase_services = ShowcaseService()
    result = showcase_services.setshowcaseitems(item_image_ids)
    if result['status'] == 'SUCCESS':
        result['status'] = True
    else:
        result['status'] = False
    return HttpResponse(json.dumps(result))

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