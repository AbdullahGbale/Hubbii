from django.shortcuts import render, redirect
from .models import Experience, Certificate, Profile, Project, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
#from .models import Profile
from django.contrib.auth.decorators import login_required
#from .forms import CustomSignupForm
from .forms import PostForm
from .models import Post
from .models import Profile
from .forms import ProfileForm

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



@login_required
def projects(request):
    # Your logic to handle the 'projects' page
    return render(request, 'projects.html')

''''
def search(request):
    query = request.GET.get('q')
    if query:
        users = User.objects.filter(username__icontains=query)
    else:
        users = User.objects.none()  # No results
    return render(request, 'search_results.html', {'users': users})
'''

@login_required
def collaborate(request):
    return render(request, 'collaborate.html')

@login_required
def portfolio(request):
    return render(request, 'portfolio.html')  # Render the portfolio template




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