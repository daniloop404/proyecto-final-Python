from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def product(request):
    return render(request, 'core/product.html')

def testimonial(request):
    return render(request, 'core/testimonial.html')

def notfound(request):
    return render(request, 'core/404.html')