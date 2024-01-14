from django.db import models

class Service(models.Model):
    description = models.CharField(max_length=255, verbose_name="Descripción")
    value = models.IntegerField(verbose_name="Valor")
    icon_class = models.CharField(max_length=255, verbose_name="Clase del Icono")
    delay = models.FloatField(verbose_name="Retraso en la animación")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description