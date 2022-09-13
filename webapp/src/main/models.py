from unicodedata import name
from django.db import models

class Item(models.Model):
    name = models.CharField("Name", max_length=250)
    description = models.CharField("Description", max_length=500)
    price = models.IntegerField("Price")