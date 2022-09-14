from django.db import models

class Item(models.Model):
    name = models.CharField("Name", max_length=250)
    description = models.CharField("Description", max_length=500)
    price = models.IntegerField("Price")
    
    def __str__(self):
        return f"{self.name} :{self.price}"

    def display_price(self):
        return "{0:.2f}".format(self.price/100)