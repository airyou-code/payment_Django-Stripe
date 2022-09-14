from django.http import JsonResponse, HttpResponse
from django.views.generic import TemplateView
from django.conf import settings
from django.shortcuts import render
from django.views import View
from django.conf import settings
from item.models import Item

import stripe
import json

stripe.api_key = settings.STRIPE_SECRET_KEY
DOMAIN = settings.DOMAIN

class SuccessView(TemplateView):
    template_name = "main/success.html"

class CancelView(TemplateView):
    template_name = "main/cancel.html"

def item(request, pk):
    product = Item.objects.get(id=pk)
    return render(request, 'main/item.html', {'item':product, 'STRIPE_SECRET_KEY':settings.STRIPE_PUBLISH_KEY})


