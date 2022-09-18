from rest_framework.viewsets import  ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .serializers import ItemSerializer, OrderSerializer

from django.http import Http404
from django.views.generic import View
from django.http import JsonResponse
from django.conf import settings
from ..models import Item, Order
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY
DOMAIN = settings.DOMAIN

class ItemAPIView(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name']
    filterset_fields = ['name', 'price']

class OrderAPIView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class BuyAPI(View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs["pk"]
        try:
            product = Item.objects.get(id=pk)
        except:
            raise Http404(f"Item {pk} not found")
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
            success_url=DOMAIN + 'success/',
            cancel_url=DOMAIN + 'cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        },status=status.HTTP_200_OK,)

class BuyOrderAPI(View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs["pk"]
        try:
            order = Order.objects.get(id=pk)
        except:
            raise Http404(f"Order {pk} not found")

        items = order.items.all()
        line_items = []
        for i in items:
            item = {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': i.price,
                        'product_data': {
                            'name': i.name,
                        },
                    },
                    'quantity': 1,
                }
            line_items.append(item)
        
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            metadata={
                "product_id": order.id
            },
            mode='payment',
            success_url=DOMAIN + '/success/',
            cancel_url=DOMAIN + '/cancel/',
        )
        
        return JsonResponse({
            'id': checkout_session.id
        },status=status.HTTP_200_OK,)
    