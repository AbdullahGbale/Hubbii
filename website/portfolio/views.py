from django.shortcuts import render, redirect
from .models import Experience, Certificate, Profile, Project, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Portfolio
from django.contrib.auth.decorators import login_required
#from .forms import CustomSignupForm
from .forms import PostForm
from .models import Post
from .models import Profile
from .forms import ProfileForm
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Project
from .forms import ProjectForm

# Home View
#def home(request):
    #return render(request, 'home.html')



# For rendering the homepage with the logged-in user's name
#@login_required
def home(request):
    return render(request, 'home.html', {'user': request.user})





# User Signup without using the default Django form template
def signup_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        UserProfile.objects.create(user=user)  # Create associated UserProfile
        messages.success(request, "Registration successful. Please log in.")
        return redirect('login')

    return render(request, 'signup.html')


'''
# if you want to use django builtin form for user sign up's

def signup_user(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create associated UserProfile
            UserProfile.objects.create(user=user)
            login(request, user)  # Log in the user after signup
            messages.success(request, "Registration successful. Welcome!")
            return redirect('home')  # Redirect to the home page or any desired page
        else:
            messages.error(request, "There was an error in the signup form. Please try again.")
    else:
        form = CustomSignupForm()
    return render(request, 'signup.html', {'form': form})
'''


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

    return render(request, 'login.html')







# User Logout
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')



# Home Page View
def home(request):
    form = UserSearchForm()
    results = None

    if request.GET.get('username'):
        form = UserSearchForm(request.GET)
        if form.is_valid():
            username = form.cleaned_data['username']
            results = User.objects.filter(username__icontains=username)  # Case-insensitive search

    return render(request, 'home.html', {'form': form, 'results': results})



# User Profile View
def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = user.post_set.all()  # Assuming posts are linked to User
    return render(request, 'profile.html', {'user': user, 'posts': posts})




# View to display project posts
@login_required
def projects(request):
    posts = Project.objects.filter(user=request.user)
    return render(request, 'projects.html', {'posts': posts})



# View to display portfolio posts
@login_required
def portfolio(request):
    posts = Portfolio.objects.filter(user=request.user)  # Only show posts of the logged-in user
    return render(request, 'portfolio.html', {'posts': posts})



# View to display certificates posts
@login_required
def certificate(request):
    posts = Collaborate.objects.filter(user=request.user)
    return render(request, 'certificate.html', {'posts': posts})




'''
@login_required
def projects(request):
    # Your logic to handle the 'projects' page
    return render(request, 'projects.html')


def search(request):
    query = request.GET.get('q')
    if query:
        users = User.objects.filter(username__icontains=query)
    else:
        users = User.objects.none()  # No results
    return render(request, 'search_results.html', {'users': users})
'''




def search_users(request):
    results = None
    form = UserSearchForm()

    if request.method == 'GET' and 'username' in request.GET:
        form = UserSearchForm(request.GET)
        if form.is_valid():
            username = form.cleaned_data['username']
            results = User.objects.filter(username__icontains=username)  # Case-insensitive search

    return render(request, 'search_users.html', {'form': form, 'results': results})






@login_required  # Ensure only logged-in users can create posts
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # Don't save to the database yet
            post.user = request.user  # Set the user field
            post.save()  # Now save to the database
            return redirect('home')  # Redirect to the home page (or another page)
    else:
        form = PostForm()

    return render(request, 'posts/create_post.html', {'form': form})



# View posts for a user
def user_posts(request, username):
    user = get_object_or_404(User, username=username)
    posts = user.posts.all()
    return render(request, 'posts/user_posts.html', {'user': user, 'posts': posts})




# Update a post
@login_required
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/update_post.html', {'form': form})





# Delete a post
@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('profile', username=request.user.username)
    return render(request, 'posts/delete_post.html', {'post': post})






def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # Retrieve all posts, most recent first
    return render(request, 'posts/post_list.html', {'posts': posts})




@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to profile page after saving
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'users/profile.html', {'form': form, 'profile': profile})



@login_required
def posts_by_category(request, category):
    posts = Post.objects.filter(category=category).order_by('-created_at')
    paginator = Paginator(posts, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/posts_by_category.html', {
        'page_obj': page_obj,
        'category': category,
    })






# View to add a Project Post
@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('project')
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})





# View to add a Certificate Post
@login_required
def add_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            certificate = form.save(commit=False)
            certificate.user = request.user
            certificate.save()
            return redirect('certificate')
    else:
        form = CertificateForm()
    return render(request, 'add_certificate.html', {'form': form})




# View to add a Portfolio Post
@login_required
def add_portfolio(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST)  # Process form data
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Assign the current user to the post
            post.save()  # Save the new post to the database
            return redirect('portfolio')  # Redirect to portfolio page after saving
    else:
        form = PortfolioForm()  # Create a new form instance
    return render(request, 'add_portfolio.html', {'form': form})  # Render the form




@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = ProjectForm(instance=project)

    return render(request, 'project_detail.html', {'form': form, 'project': project})


'''
@login_required
def collaborate(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.user != project.user:  # Prevent project owner from collaborating with their project
        project.collaborators.add(request.user)
        project.save()
    return redirect('project_detail', project_id=project.id)
'''



def collaborate(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        project.collaborators.add(request.user)
        messages.success(request, 'You have joined the collaboration!')
        return redirect('collaborate', project_id=project.id)
    return render(request, 'collaborate.html', {'project': project})

