
from django.urls import path
from soap_service.views import django_soap_app

urlpatterns = [
    path('soap/', django_soap_app),
    # Add other paths if needed
]
