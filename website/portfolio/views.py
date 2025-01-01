from django.shortcuts import render, redirect
from .models import Experience, Certificate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.decorators import login_required

# Home View
#def home(request):
    #return render(request, 'home.html')



# For rendering the homepage with the logged-in user's name
#@login_required
def home(request):
    return render(request, 'home.html', {'user': request.user})




# User Signup
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


@login_required
def collaborate(request):
    return render(request, 'collaborate.html')

@login_required
def portfolio(request):
    return render(request, 'portfolio.html')  # Render the portfolio template



