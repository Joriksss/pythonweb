from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, '')

def About(request):
    return render(request, 'About.html')