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
            file_name = '%s%s'%(settings.MEDIA_URL, item_img.name)
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
    
    def getitemsofcategoryid(self,category_id):
        items = []
        item_list = None
        if(category_id == 0):
            item_list = Item.objects.all()
        else:
            item_list = Item.objects.filter(category_id=category_id)
        
        for item in item_list:
            image = ''
            if item.itemimage_set is not None and item.itemimage_set.count() > 0:
                image = '%s%s'%(settings.MEDIA_URL, item.itemimage_set.all()[0].image.name)
            it = {"id":item.id,"name":item.name,"image":image}
            items.append(it)
        
        return items
    
    def getitem(self,item_id):
        item_obj = {}
        try:
            item = Item.objects.get(id=item_id)
            item_obj = {'id':item.id,'name':item.name,'description':item.description,'category':item.category.id,'images':[]}
            if item.itemimage_set is not None and item.itemimage_set.count() > 0:
                for img in item.itemimage_set.all():
                    img_obj = {'link':'%s%s'%(settings.MEDIA_URL, img.image.name)}
                    item_obj['images'].append(img_obj)
        except:
            pass
        
        result = {
                  'status':'SUCCESS',
                  'data': 
                  {
                    'item':item_obj
                  }
                 }
        return result

class ImageUploader(models.ModelForm):
    class Meta:
        model = ItemImage
    