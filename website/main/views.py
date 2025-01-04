
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Project, Certificate, Portfolio
from django.contrib.auth.models import User
from .forms import ProjectForm


# Create your views here:


# Home View
#@login_required
def home(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'main/home.html', {'profile': profile})



# Profile View
@login_required
def profile(request):
    user = get_object_or_404(User, username=username)
    return render(request, 'main/profile.html', {'user': user})


'''
# Projects View
@login_required
def projects(request):
    user_projects = Project.objects.filter(owner=request.user)
    all_projects = Project.objects.exclude(owner=request.user)
    return render(request, 'main/projects.html', {
        'user_projects': user_projects,
        'all_projects': all_projects
    })
'''


@login_required
def projects(request):
    user_projects = Project.objects.filter(user=request.user)
    other_projects = Project.objects.exclude(user=request.user)

    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('projects')
    else:
        form = ProjectForm()

    context = {
        'user_projects': user_projects,
        'other_projects': other_projects,
        'form': form,
    }
    return render(request, 'main/projects.html', context)



# Certificates View
@login_required
def certificates(request):
    certificates = Certificate.objects.filter(user=request.user)
    return render(request, 'main/certificates.html', {'certificates': certificates})



# Portfolio View
@login_required
def portfolio(request):
    try:
        portfolio = Portfolio.objects.get(user=request.user)
    except Portfolio.DoesNotExist:
        portfolio = None  # Handle the case where no portfolio exists
    return render(request, 'main/portfolio.html', {'portfolio': portfolio})



# Search View
@login_required
def search(request):
    query = request.GET.get('q', '').strip()
    results = User.objects.filter(username__icontains=query) if query else []
    return render(request, 'main/search.html', {'query': query, 'results': results})




def default_profile(request):
    # Render a page or redirect as needed
    return render(request, 'main/default_profile.html')