from cakeshop.csmodels.models import Item, ItemCategory
from cakeshop.csmodels.models import ItemImage
from cakeshop import settings
from django.forms import models

class ItemService(object):    
    def saveitem(self,item_name,item_category,item_description,files):   
        images = []     
        category = ItemCategory.objects.get(id=item_category)
        item = Item(name=item_name,description=item_description,category=category)
        item.save()
        
        for key in files.keys():
            item_img = files.get(key)
            file_name = '%s/%s'%(settings.MEDIA_URL, item_img.name)
            images.append(file_name)
            img_handle = open('%s/%s'%(settings.MEDIA_ROOT, item_img.name),'wb+')
            for chunk in item_img.chunks():
                img_handle.write(chunk)
            img = ItemImage(image=item_img.name,item=item)
            img.save()
        
        result = {
                  'status':'SUCCESS',
                  'data': 
                  {
                    'item_id':item.id,
                    'images':images
                  }
                 }
        return result

class ImageUploader(models.ModelForm):
    class Meta:
        model = ItemImage
    