from django.db import models
from cakeshop import settings

class ItemCategory(models.Model):
    name = models.CharField(max_length=100)

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    category = models.ForeignKey(ItemCategory)

class ItemImage(models.Model):
    image = models.ImageField(upload_to=settings.MEDIA_URL,max_length=400)
    item = models.ForeignKey(Item)