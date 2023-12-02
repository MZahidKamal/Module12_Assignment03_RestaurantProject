from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request, 'about_us_app/contact.html')

def about_us(request):
    return render(request, 'about_us_app/about_us.html')
