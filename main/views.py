from django.views.generic import TemplateView
from django.http import Http404
from django.conf import settings
from django.shortcuts import render
from django.conf import settings
from item.models import Item, Order

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY
DOMAIN = settings.DOMAIN

class SuccessView(TemplateView):
    template_name = "main/success.html"
Class indexView(TemplateView):
    template_name = "main/success.html"

class CancelView(TemplateView):
    template_name = "main/cancel.html"

def item(request, pk):
    try:
        product = Item.objects.get(id=pk)
    except:
        raise Http404(f"Item {pk} not found")
    return render(request, 'main/item.html', {'item':product, 'STRIPE_SECRET_KEY':settings.STRIPE_PUBLISH_KEY})

def order(request, pk):
    try:
        order = Order.objects.get(id=pk)
    except:
        raise Http404(f"Order {pk} not found")
    return render(request, 'main/order.html', {'items':order.items.all(), 'id_order':order.id, 'STRIPE_SECRET_KEY':settings.STRIPE_PUBLISH_KEY})




