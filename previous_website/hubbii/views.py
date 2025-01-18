# hubbii/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')  # Render the 'home.html' template

