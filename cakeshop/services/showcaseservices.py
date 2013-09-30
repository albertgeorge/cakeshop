from cakeshop.csmodels.models import ItemImage
from cakeshop import settings

class ShowcaseService(object):
    def getselectedshowcaseitems(self):
        showcase_items = ItemImage.objects.all()
        showcase=[]
        if showcase_items is not None:
            for item in showcase_items:
                show_case = {"id":item.id,"image":'%s%s'%(settings.MEDIA_URL, item.image.name),"is_showcase":item.is_showcase}
                showcase.append(show_case)
                
        result = {
              'status':'SUCCESS',
              'data': 
              {
                'showcase':showcase
              }
             }
        return result
    
    def setshowcaseitems(self,items):
        result = {'status':'SUCCESS',}
        items = items.split(",")
        if items is not None and len(items) > 0:
            ItemImage.objects.filter(is_showcase=True).update(is_showcase=False)
            ItemImage.objects.filter(id__in=items).update(is_showcase=True)
        
        return result