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
    description = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    project_link = models.URLField(null=True, blank=True)
    progress = models.CharField(max_length=100, null=True, blank=True)  # Example: "Completed", "In Progress"

    def __str__(self):
        return self.title

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

# Portfolio Model
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


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()  # Ensure this exists
    image = models.ImageField(upload_to='images/')  # Ensure this exists
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title