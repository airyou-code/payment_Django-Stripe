from django.http import JsonResponse, HttpResponse
from django.views.generic import TemplateView
from django.conf import settings
from django.shortcuts import render
from django.views import View
from django.conf import settings
from .models import Item

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

def buy(request, pk):
    product = Item.objects.get(id=pk)
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': product.price,
                    'product_data': {
                        'name': product.name,
                        # 'images': ['https://i.imgur.com/EHyR2nP.png'],
                    },
                },
                'quantity': 1,
            },
        ],
        metadata={
            "product_id": product.id
        },
        mode='payment',
        success_url=DOMAIN + '/success/',
        cancel_url=DOMAIN + '/cancel/',
    )
    return JsonResponse({
        'id': checkout_session.id
    })
    # product = Item.objects.get(id=pk)
    pass


