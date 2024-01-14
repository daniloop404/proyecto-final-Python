from django.db import models

class Social(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre Red Social")
    link = models.URLField(verbose_name="Enlace")
    members = models.ForeignKey('Member', related_name='social_links', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Miembro")

    created = models.DateField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "red social"
        verbose_name_plural = "redes sociales"

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    role = models.CharField(max_length=50, verbose_name="Rol")
    image = models.ImageField(upload_to='team', verbose_name="Imagen")

    created = models.DateField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "miembro"
        verbose_name_plural = "miembros"

    def __str__(self):
        return self.name