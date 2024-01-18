from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html')


def contact(request):
    return render(request, 'core/contact.html')


def notfound(request):
    return render(request, 'core/404.html')