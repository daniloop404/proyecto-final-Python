# Generated by Django 5.0.1 on 2024-01-11 19:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("service", "0002_servicedata_delete_serviceinfo"),
    ]

    operations = [
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.CharField(max_length=255, verbose_name="Descripción"),
                ),
                ("value", models.IntegerField(verbose_name="Valor")),
                (
                    "icon_class",
                    models.CharField(max_length=255, verbose_name="Clase del Icono"),
                ),
                ("delay", models.FloatField(verbose_name="Retraso en la animación")),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name="ServiceData",
        ),
    ]
