from django.contrib import admin
from .models import Social  # Make sure to import the Social model

# Register your models here.
class SocialAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Social, SocialAdmin)