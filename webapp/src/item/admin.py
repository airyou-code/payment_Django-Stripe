from django.contrib import admin
from .models import Item
# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price"]
    search_fields = ["id"]
    list_filter = ["price"]

admin.site.register(Item, ItemAdmin)
