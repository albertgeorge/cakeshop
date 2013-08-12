from django.db import models
from cakeshop import settings

class ItemCategory(models.Model):
    name = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    category = models.ForeignKey(ItemCategory)
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['creation_date']

class ItemImage(models.Model):
    image = models.ImageField(upload_to=settings.MEDIA_URL,max_length=400)
    item = models.ForeignKey(Item)
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['creation_date']