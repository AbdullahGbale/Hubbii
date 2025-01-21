
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Rating, Comment, CollaborationRequest, Reaction, Profile
from .forms import ProjectForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import get_user_model
from .forms import SignupForm
from .forms import SignupForm





'''
def home(request):
    projects = Project.objects.all()
    return render(request, 'main/home.html', {'projects': projects})


def home(request):
    projects = Project.objects.order_by('-created_at')[:10]  # Get the 10 most recent projects (adjust as needed)
    context = {'projects': projects}
    return render(request, 'main/home.html', context)
'''


def home(request):
    latest_projects = Project.objects.order_by('-created_at')[:10]  # Fetch the 3 latest projects
    return render(request, 'main/home.html', {'latest_projects': latest_projects})



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)  # Include uploaded files
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = SignupForm()
    context = {'form': form}
    return render(request, 'main/signup.html', context)





def profile(request, username):
    user = get_object_or_404(User, username=username)
    # Add logic to retrieve and display user profile information
    context = {'user': user}
    return render(request, 'main/profile.html', context)


'''
@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect('home')  # Redirect to the home page after creating the project
    else:
        form = ProjectForm()
    return render(request, 'main/create_project.html', {'form': form})
'''



@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)  # Handle potential image uploads
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            messages.success(request, 'Project created successfully!')
            return redirect('project_detail', project_id=project.id)
        else:
            messages.error(request, 'There was an error in the form. Please correct it.')
    else:
        form = ProjectForm()
    return render(request, 'main/create_project.html', {'form': form})








def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    comment_form = CommentForm()

    if request.method == 'POST' and 'comment_submit' in request.POST: # Handle Comment
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.project = project
            comment.user = request.user
            comment.save()
            return redirect('project_detail', project_id=project_id)

    context = {'project': project, 'comment_form': comment_form}
    return render(request, 'main/project_detail.html', context)



'''
@login_required
def edit_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.user != project.owner:
        return redirect('home')  # Or display an error message
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'main/edit_project.html', {'form': form, 'project': project})
'''


@login_required
def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id, owner=request.user)  # Ensure owner can edit
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)  # Handle potential image edits
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('project_detail', project_id=project.id)
        else:
            messages.error(request, 'There was an error in the form. Please correct it.')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'main/edit_project.html', {'form': form, 'project': project})



@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.user != project.owner:
        return redirect('home')
    if request.method == 'POST':
        project.delete()
        return redirect('home')
    return render(request, 'main/delete_project.html', {'project': project})





@login_required
def rate_project(request, project_id, rating):
    project = get_object_or_404(Project, pk=project_id)
    try:
        Rating.objects.update_or_create(user=request.user, project=project, defaults={'rating': rating})
        project.total_rating = sum(r.rating for r in project.ratings.all())
        project.num_ratings = project.ratings.count()
        project.save()
        return JsonResponse({'status':'success', 'average_rating': project.average_rating()})
    except Exception as e:
        return JsonResponse({'status':'error', 'message':str(e)})
    



@login_required
def react_project(request, project_id, reaction_type):
    project = get_object_or_404(Project, pk=project_id)
    try:
        Reaction.objects.update_or_create(user=request.user, project=project, defaults={'reaction_type': reaction_type})
        return JsonResponse({'status':'success'})
    except Exception as e:
        return JsonResponse({'status':'error', 'message':str(e)})






def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    comment_form = CommentForm()
    has_sent_request = False

    if request.user.is_authenticated:
        has_sent_request = CollaborationRequest.objects.filter(
            sender=request.user, receiver=project.owner, project=project
        ).exists()
    # ... handle comment submissions

    context = {'project': project, 'comment_form': comment_form, 'has_sent_request': has_sent_request}
    return render(request, 'main/project_detail.html', context)



@login_required
def send_collaboration_request(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        if request.user == project.owner:
            messages.error(request, "You can't send a collaboration request to yourself.")
            return redirect('project_detail', project_id=project_id)

        if CollaborationRequest.objects.filter(sender=request.user, receiver=project.owner, project=project).exists():
            messages.info(request, "You have already sent a collaboration request for this project.")
            return redirect('project_detail', project_id=project_id)

        CollaborationRequest.objects.create(sender=request.user, receiver=project.owner, project=project)
        messages.success(request, "Collaboration request sent successfully.")
        return redirect('project_detail', project_id=project_id)
    return redirect('project_detail', project_id=project_id)



@login_required
def accept_collaboration_request(request, request_id):
    collaboration_request = get_object_or_404(CollaborationRequest, pk=request_id, receiver=request.user)
    if request.method == 'POST':
        collaboration_request.accepted = True
        collaboration_request.save()
        messages.success(request, "Collaboration request accepted.")
        return redirect('profile', username=request.user.username) # Redirect to profile or project page
    return redirect('profile', username=request.user.username)




@login_required
def reject_collaboration_request(request, request_id):
    collaboration_request = get_object_or_404(CollaborationRequest, pk=request_id, receiver=request.user)
    if request.method == 'POST':
        collaboration_request.delete()
        messages.success(request, "Collaboration request rejected.")
        return redirect('profile', username=request.user.username)
    return redirect('profile', username=request.user.username)




def list_projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'main/project_list.html', context)





def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile, created = Profile.objects.get_or_create(user=user)
    projects = Project.objects.filter(owner=user)
    is_following = False
    if request.user.is_authenticated:
        is_following = profile.followers.filter(id=request.user.id).exists()
    context = {'user': user, 'profile': profile, 'projects': projects, 'is_following': is_following}
    return render(request, 'main/profile.html', context)




@login_required
def follow_user(request, username):
    target_user = get_object_or_404(User, username=username)
    target_profile = get_object_or_404(Profile, user=target_user)
    if request.user != target_user:
        if target_profile.followers.filter(id=request.user.id).exists():
            target_profile.followers.remove(request.user)
            messages.success(request, f"You have unfollowed {target_user.username}")
        else:
            target_profile.followers.add(request.user)
            messages.success(request, f"You are now following {target_user.username}")
    return redirect('profile', username=username)




'''
@login_required
def like_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.user in project.likes.all():
        project.likes.remove(request.user)
    else:
        project.likes.add(request.user)
    return redirect('project_detail', project_id=project_id)
'''



@login_required
def like_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.user in project.likes.all():
        project.likes.remove(request.user)
        liked = False
    else:
        project.likes.add(request.user)
        liked = True

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest': #For AJAX requests
        return JsonResponse({'likes_count': project.total_likes(), 'liked': liked})
    else:
        return redirect('project_detail', project_id=project_id)






def show_default_profile(request):
    # Your logic to display the default profile content
    context = {'message': 'This is the default profile.'}
    return render(request, 'main/default_profile.html', context)







