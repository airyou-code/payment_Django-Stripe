from django.urls import path
from . import views

urlpatterns = [
    path('cancel/', views.CancelView.as_view(), name='cancel'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('buy/<int:pk>/', views.buy),
    path('item/<int:pk>/', views.item)
]