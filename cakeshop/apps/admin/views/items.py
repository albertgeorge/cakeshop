from django.template import RequestContext
from django.shortcuts import render_to_response

def add_edit_item(request):    
    return render_to_response('item.html', context_instance = RequestContext(request))