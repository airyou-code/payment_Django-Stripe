from django.contrib import admin
from .models import Item, Order
# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price"]
    search_fields = ["id"]
    list_filter = ["price"]

class OrderAdmin(admin.ModelAdmin):
    list_display = ["id"]
    search_fields = ["id"]

admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
