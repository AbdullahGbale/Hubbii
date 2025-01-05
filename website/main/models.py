from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Profile Model to extend User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="main_profile")
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='default.jpg')
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    github = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username




# Project Model
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='portfolio_images/', blank=True, null=True)
    description = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    project_link = models.URLField(null=True, blank=True)
    technologies = models.CharField(max_length=255, blank=True, null=True)
    progress = models.CharField(max_length=100, null=True, blank=True)  # Example: "Completed", "In Progress"

    def __str__(self):
        return self.title






'''
# Second project model
class Project(models.Model):
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/', blank=True, null=True)
    project_link = models.URLField(blank=True, null=True)
    technologies = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
'''


# Certificate Model
class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificates')
    title = models.CharField(max_length=200)
    issued_by = models.CharField(max_length=200)
    certificate_image = models.ImageField(upload_to='certificates/', blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_issued = models.DateField()

    def __str__(self):
        return self.title
    





''''
# first Portfolio Model
class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.TextField()
    experience = models.TextField()
    projects = models.TextField()
   
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    github = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Portfolio"
    
    # second portfolio model
    class PortfolioItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/', blank=True, null=True)  # Optional image
    project_link = models.URLField(blank=True, null=True)
    technologies = models.CharField(max_length=255, blank=True, null=True)  # e.g., "Python, Django, JavaScript"

    def __str__(self):
        return self.title
'''



# Third portfolio model
class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.TextField(blank=True, null=True) # Could be a ManyToManyField later
    your_DP_image = models.ImageField(upload_to='portfolio_images/', blank=True, null=True)  # Optional image
    about_you = models.TextField()
    project_link = models.URLField(blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    github = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Portfolio"





class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    skills = models.CharField(max_length=255)  # Example: "Graphics Designer, Software Engineer"
    technologies = models.CharField(max_length=255, blank=True, null=True)  # e.g., "Python, Django, JavaScript"
    image = models.ImageField(upload_to='portfolio_posts/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.user.username}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"