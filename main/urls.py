from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('cancel/', views.CancelView.as_view(), name='cancel'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('item/<int:pk>/', views.item),
    path('order/<int:pk>/', views.order),
    path('api/', include('item.urls'))
]
