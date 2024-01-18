from django.shortcuts import render
from .models import Testimonial

def testimonial(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonial/testimonial.html', {'testimonials': testimonials})