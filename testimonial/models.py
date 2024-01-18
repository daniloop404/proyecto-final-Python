from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='testimonial_images/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name