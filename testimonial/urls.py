from django.urls import path
from .views import testimonial

urlpatterns = [
    path('', testimonial, name='testimonial'),
    # Add other URLs if needed
]