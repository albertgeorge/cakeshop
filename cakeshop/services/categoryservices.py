from cakeshop.csmodels.models import ItemCategory

class CategoryService(object):
    def get_categories(self):
        cat_list= []
        all_categories = ItemCategory.objects.all()
        for category in all_categories:
            cat = {"id":category.id,"name":category.name}
            cat_list.append(cat)
        return cat_list
    
    def add_category(self,name):
        obj, created = ItemCategory.objects.get_or_create(name=name)
        result = {
                  'status':True
                 }
        return result
        