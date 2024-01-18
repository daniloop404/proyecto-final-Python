# views.py
from django.shortcuts import render
from .models import About

def about(request):
    about_pages = About.objects.all()
    return render(request, 'about/about.html', {'pages': about_pages})