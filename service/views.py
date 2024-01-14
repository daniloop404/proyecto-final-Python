from django.shortcuts import render
from .models import Service

def service_view(request):
    service_data = Service.objects.all()
    return render(request, 'service/service.html', {'service_data': service_data})