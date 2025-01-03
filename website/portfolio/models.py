
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from django import forms
from django.db.models.signals import post_save
from django.dispatch import receiver





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"




class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(default='2025-01-01')
    end_date = models.DateField(null=True, blank=True)
    project_link = models.URLField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    progress = models.IntegerField(default=0)  # Progress tracking (0-100)
    collaborators = models.ManyToManyField(User, related_name='collaborating_projects', blank=True)  # Track collaborators

    def collaborator_count(self):
        return self.collaborators.count()

    def __str__(self):
        return self.title



class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Links the certificate to a user
    title = models.CharField(max_length=100) # The title of the certificate (e.g., "Web Development Certification")
    description = models.TextField()  # A description of the certificate
    issue_date = models.DateField() 
    issued_by = models.CharField(max_length=255, default='Unknown') # The institution/organization that issued the certificate
    certificate_image = models.ImageField(upload_to='certificates/', blank=False)
    def __str__(self):
        return f"{self.title} ({self.user.username})"




class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # Null if still ongoing
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.position} at {self.company} ({self.user.username})"


class CustomSignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')



class Post(models.Model):
    CATEGORY_CHOICES = [
        ('Portfolio', 'Portfolio'),
        ('Project', 'Project'),
        ('Certificate', 'Certificate'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    


class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()  # Ensure this field exists
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title