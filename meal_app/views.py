from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'meal_app/home.html')

def meals(request):
    return render(request, 'meal_app/meals.html')
