from django.urls import include, path
from rest_framework import routers
from .views import ProductViewSet

urlpatterns = [
    # інші URL-адреси
    path('products/create/', create_product),
    path('products/update/<int:pk>/', update_product),
    path('products/delete/<int:pk>/', delete_product),
]
