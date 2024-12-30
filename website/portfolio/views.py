from django.shortcuts import render, redirect
from .models import PortfolioSection, Contact, Experience, Skill
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Home View
def home(request):
    return render(request, 'portfolio/home.html')



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



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

