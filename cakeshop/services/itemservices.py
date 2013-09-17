from cakeshop.csmodels.models import Item, ItemCategory
from cakeshop.csmodels.models import ItemImage
from cakeshop import settings
from django.forms import models

class ItemService(object):    
    def saveitem(self,item_name,item_category,item_description,files,item_id):   
        images = []     
        category = ItemCategory.objects.get(id=item_category)
        if item_id is None:
            item = Item(name=item_name,description=item_description,category=category)        
            item.save()    
        else:
            item = Item.objects.get(id=item_id)
            item.name = item_name
            item.category = category
            item.description = item_description
            item.save()
            try:
                item_images = ItemImage.objects.get(item=item)       
                if item_images is not None and len(item_images) > 0:
                    for img in item_images:
                        images.append('%s%s'%(settings.MEDIA_URL, img.name))
            except:
                pass
                                    
        
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
                    'item':item,
                    'images':images
                  }
                 }
        return result
    
    def getitemsofcategoryid(self,category_id):
        items = []
        item_list = None
        if(category_id == '0' or category_id == 0):
            item_list = Item.objects.all()
        else:
            item_list = Item.objects.filter(category__id=category_id)
        
        for item in item_list:
            image = ''
            if item.itemimage_set is not None and item.itemimage_set.count() > 0:
                image = '%s%s'%(settings.MEDIA_URL, item.itemimage_set.all()[0].image.name)
            it = {"id":item.id,"name":item.name,"image":image}
            items.append(it)
        
        result = {
                  'status':'SUCCESS',
                  'data': 
                  {
                    'items':items
                  }
                 }
        return result
    
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
    