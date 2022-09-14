from django.urls import path
from .api import views
from rest_framework import routers
from .api.views import ItemAPIView


router1 = routers.DefaultRouter()
router1.register(r'item', ItemAPIView, basename='item')

urlpatterns = [
    path('buy/<int:pk>/', views.BuyAPI.as_view(), name='buy')
] + router1.urls