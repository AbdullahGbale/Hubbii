
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Project, Certificate, Portfolio
from django.contrib.auth.models import User


# Create your views here:


# Home View
#@login_required
def home(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'main/home.html', {'profile': profile})



# Profile View
@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'main/profile.html', {'profile': profile})



# Projects View
@login_required
def projects(request):
    user_projects = Project.objects.filter(owner=request.user)
    all_projects = Project.objects.exclude(owner=request.user)
    return render(request, 'main/projects.html', {
        'user_projects': user_projects,
        'all_projects': all_projects
    })



# Certificates View
@login_required
def certificates(request):
    certificates = Certificate.objects.filter(user=request.user)
    return render(request, 'main/certificates.html', {'certificates': certificates})



# Portfolio View
@login_required
def portfolio(request):
    portfolio = Portfolio.objects.get(user=request.user)
    return render(request, 'main/portfolio.html', {'portfolio': portfolio})



# Search View
@login_required
def search(request):
    query = request.GET.get('q')
    results = User.objects.filter(username__icontains=query)
    return render(request, 'main/search.html', {'results': results})




def default_profile(request):
    # Render a page or redirect as needed
    return render(request, 'main/default_profile.html')