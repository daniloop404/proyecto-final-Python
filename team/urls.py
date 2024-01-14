from django.urls import path
from .views import team

urlpatterns = [
    path('', team, name='team'),
    # Add other URLs if needed
]