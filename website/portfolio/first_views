from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import UserProfile, Project

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')


def profile_detail(request, user_id):
    # Ensure a profile is created if it doesn’t exist
    profile, created = UserProfile.objects.get_or_create(user_id=user_id)

    return render(request, 'portfolio/profile.html', {'profile': profile, 'created': created})


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Account created successfully!')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'portfolio/register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome, {user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'portfolio/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('home')

from django.shortcuts import render
from .models import Project, Certificate

def projects(request):
    projects = Project.objects.all()  # Fetch all projects from the database
    return render(request, 'portfolio/projects.html', {'projects': projects})

def certificate_list(request):
    certificates = Certificate.objects.all()  # Fetch all certificates from the database
    return render(request, 'portfolio/certificates.html', {'certificates': certificates})





def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        message = request.POST['message']
        email = request.POST['email']
        send_mail(f"Message from {name}", message, email, ['admin@example.com'])
    return render(request, 'portfolio/contact.html')

