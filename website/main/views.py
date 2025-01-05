
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Project, Certificate, Portfolio, Post, Comment
from django.contrib.auth.models import User
from .forms import ProjectForm, PostForm, CommentForm
from django.shortcuts import get_object_or_404 
from django.http import HttpResponse




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






# Certificates View
@login_required
def certificates(request):
    certificates = Certificate.objects.filter(user=request.user)
    return render(request, 'main/certificates.html', {'certificates': certificates})




# Search View
@login_required
def search(request):
    query = request.GET.get('q', '').strip()
    results = User.objects.filter(username__icontains=query) if query else []
    return render(request, 'main/search.html', {'query': query, 'results': results})




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



