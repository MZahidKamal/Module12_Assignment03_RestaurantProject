from django.urls import path, include
from .views import contact, about_us

urlpatterns = [
    path('contact/', contact),
    path('about_us/', about_us),
]
