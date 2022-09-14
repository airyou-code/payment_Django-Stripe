from rest_framework.viewsets import  ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .serializers import ItemSerializer

from django.views.generic import View
from django.http import JsonResponse
from django.conf import settings
from ..models import Item
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY
DOMAIN = settings.DOMAIN

class ItemAPIView(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name']
    filterset_fields = ['name', 'price']

class BuyAPI(View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs["pk"]
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
    