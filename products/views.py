# products/views.py
from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def category_products(request, category_id=None):
    categories = Category.objects.all()
   
    if category_id:
        category = get_object_or_404(Category, pk=category_id)
        products = Product.objects.filter(category=category)
        return render(request, 'products/product.html', {'category': category, 'products': products})
   
    return render(request, 'products/product.html', {'categories': categories})

def product_details(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'products/product_detail.html', {'category': category, 'products': products})