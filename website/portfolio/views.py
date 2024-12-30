from django.shortcuts import render, redirect
from .models import PortfolioSection, Contact, Experience, Skill
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserProfile


# Home View
def home(request):
    return render(request, 'portfolio/home.html')






def index(request):
    return render(request, 'portfolio/index.html')







# User Signup
def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        UserProfile.objects.create(user=user)  # Create associated UserProfile
        messages.success(request, "Registration successful. Please log in.")
        return redirect('login')

    return render(request, 'auth/register.html')







# User Login
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'auth/login.html')







# User Logout
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')







def projects(request):
    # Your logic to handle the 'projects' page
    return render(request, 'portfolio/projects.html')





def profile_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)  # Get the user or return a 404
    profile = user.userprofile  # Access the related UserProfile object (assuming a OneToOneField relationship)
    return render(request, 'profile/detail.html', {'user': user, 'profile': profile})







# Portfolio Section Views
def portfolio_section_list(request):
    sections = PortfolioSection.objects.filter(user=request.user)
    return render(request, 'portfolio/portfolio_section_list.html', {'sections': sections})







def portfolio_section_add(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'portfolio/portfolio_section_add.html')







# Contact Views
def contact_detail(request):
    contact = Contact.objects.get(user=request.user)
    return render(request, 'portfolio/contact_detail.html', {'contact': contact})







def contact_edit(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'portfolio/contact_edit.html')








# Experience Views
def experience_list(request):
    experiences = Experience.objects.filter(user=request.user)
    return render(request, 'portfolio/experience_list.html', {'experiences': experiences})








def experience_add(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'portfolio/experience_add.html')








# Skill Views
def skill_list(request):
    skills = Skill.objects.filter(user=request.user)
    return render(request, 'portfolio/skill_list.html', {'skills': skills})






def skill_add(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'portfolio/skill_add.html')

