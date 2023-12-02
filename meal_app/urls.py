from django.urls import path, include
from .views import home, meals

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('menu/', meals, name='menu'),
    path('menu/', meals, name='menu'),
]
