from django.contrib import admin
from .models import Testimonial

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'occupation', 'created', 'updated')

admin.site.register(Testimonial, TestimonialAdmin)