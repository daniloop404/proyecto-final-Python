# models.py
from django.db import models
from ckeditor.fields import RichTextField

class About(models.Model):
    title = models.CharField(max_length=255)
    content=RichTextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title  # Adjust the name of the URL pattern if needed