from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    
class ItemCategory(models.Model):
    name = models.CharField(max_length=100)
    item = models.ForeignKey(Item, blank=True,null=True)

class ItemImage(models.Model):
    imageurl = models.CharField(max_length=400)
    linktype = models.CharField(max_length=4)
    item = models.ForeignKey(Item)