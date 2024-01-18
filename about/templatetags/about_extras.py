# __pages_extras.py
from django import template
from about.models import About

register = template.Library()

@register.simple_tag
def get_about():
    about = About.objects.all()
    return about