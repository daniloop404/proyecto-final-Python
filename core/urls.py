from django.contrib import admin
from django.urls import path
from core import views as core_views
urlpatterns = [
    path("", core_views.home, name="home"),
    path("about/", core_views.about, name="about"),
    path("contact/", core_views.contact, name="contact"),
    path("product/", core_views.product, name="product"),
    path("testimonial/", core_views.testimonial, name="testimonial"),
    path("admin/", admin.site.urls),
]
