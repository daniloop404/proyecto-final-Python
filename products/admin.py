# admin.py
from django.contrib import admin
from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_range', 'category', 'image', 'created', 'updated')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    readonly_fields = ('created', 'updated')

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)