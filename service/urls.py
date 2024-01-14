from django.urls import path
from .views import service_view

urlpatterns = [
    path('', service_view, name='service'),
    # Add other URLs if needed
]