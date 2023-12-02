from django.urls import path, include
from .views import home, meals

urlpatterns = [
    path('', home),
    path('home/', home),
    path('menu/', meals),
]
