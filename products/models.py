# models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to='category_images/', verbose_name="Imagen")
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de edición")

    def __str__(self):
        return self.name

class Product(models.Model):
    price_range = models.CharField(max_length=20, help_text='Price range, e.g., $11 - $99', verbose_name="Rango de precio")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoría")
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to='product_images/', verbose_name="Imagen")
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de edición")

    def __str__(self):
        return self.name