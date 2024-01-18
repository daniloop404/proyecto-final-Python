# products/urls.py
from django.urls import path
from .views import category_products, product_details

urlpatterns = [
    path('', category_products, name='products'),
    path('category/<int:category_id>/', category_products, name='category_products'),
    path('product/<int:category_id>/', product_details, name='product_details'),  # Use 'product_id' instead of 'category_id'
    # Add other URLs if needed
]