
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Project, Post, Comment
from django.contrib.auth.models import User
from .forms import ProjectForm, PostForm, CommentForm
from django.shortcuts import get_object_or_404 
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Project



# Create your views here:



def home(request):
    projects = Project.objects.order_by('-created_at')
    return render(request, 'main/home.html', {'projects': projects})



def custom_logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to your homepage or another URL





# Profile View
@login_required
def profile(request):
    user = get_object_or_404(User, username=username)
    return render(request, 'main/profile.html', {'user': user})






# Certificates View
@login_required
def certificates(request):
    certificates = Certificate.objects.filter(user=request.user)
    return render(request, 'main/certificates.html', {'certificates': certificates})




# Search View
def search(request):
    query = request.GET.get('q', '')  # Get the search query from the request
    users = User.objects.filter(username__icontains=query) if query else []
    projects = Project.objects.filter(name__icontains=query) if query else [] 
    portfolios = Portfolio.objects.filter(name__icontains=query) if query else []  

    context = {
        'query': query,
        'users': users,
        'projects': projects,
        'portfolios': portfolios,
    }
    return render(request, 'main/search_results.html', context)


def default_profile(request):
    # Render a page or redirect as needed
    return render(request, 'main/default_profile.html')




@login_required
def projects(request):
    user_projects = Project.objects.filter(user=request.user)

    if request.method == "POST":
        if 'create-project' in request.POST:
            form = ProjectForm(request.POST, request.FILES)
            if form.is_valid():
                project = form.save(commit=False)
                project.user = request.user
                project.save()
                return redirect('projects')
        elif 'update-project' in request.POST:
            project_id = request.POST.get('project_id')
            project = get_object_or_404(Project, pk=project_id)
            if project.user == request.user:
                form = ProjectForm(request.POST, request.FILES, instance=project)
                if form.is_valid():
                    form.save()
                    return redirect('projects')

    else:
        form = ProjectForm()

    context = {
        'user_projects': user_projects,
        'form': form,
    }
    return render(request, 'main/projects.html', context)




@login_required
def project_delete(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if project.user == request.user:
        project.delete()
    return redirect('projects')







@login_required
def portfolio(request):
    posts = Post.objects.all().order_by('-created_at')
    comment_form = CommentForm()
    context = {'posts': posts, 'comment_form': comment_form}
    return render(request, 'main/portfolio.html', context)





@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('portfolio')
    else:
        form = PostForm()
    return render(request, 'main/create_post.html', {'form': form})




@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('portfolio')
    else:
        form = PostForm(instance=post)
    return render(request, 'main/update_post.html', {'form': form})




@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    post.delete()
    return redirect('portfolio')




@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
    return redirect('portfolio')





def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after signup
    else:
        form = UserCreationForm()
    return render(request, 'main/signup.html', {'form': form})






def signin_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')





from django.template.loader import get_template

def debug_template(request):
    template = get_template('login.html')  # Replace with your template name
    return HttpResponse("Template found successfully!")



def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    projects = user.projects.all()
    return render(request, 'main/profile.html', {'profile_user': user, 'projects': projects})
