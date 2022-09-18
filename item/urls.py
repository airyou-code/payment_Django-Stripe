from django.urls import path
from .api import views
from rest_framework import routers
from .api.views import ItemAPIView, OrderAPIView


router = routers.DefaultRouter()
router.register(r'item', ItemAPIView, basename='item')
router.register(r'order', OrderAPIView, basename='order')

urlpatterns = [
    path('buy/<int:pk>/', views.BuyAPI.as_view(), name='buy'),
    path('buyorder/<int:pk>/', views.BuyOrderAPI.as_view(), name='buyorder')
] + router.urls