
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.user.username

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='project_images/', blank=True)

    def __str__(self):
        return self.title


class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    issue_date = models.DateField()
    issued_by = models.CharField(max_length=255, default='Unknown')
    certificate_image = models.ImageField(upload_to='certificates/', blank=False)
    def __str__(self):
        return f"{self.title} ({self.user.username})"


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(default=0)  # Percentage or rating (0-100)

    def __str__(self):
        return f"{self.name} ({self.user.username})"


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # Null if still ongoing
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.position} at {self.company} ({self.user.username})"


class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)

    def __str__(self):
        return self.user.username

class PortfolioSection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} ({self.user.username})"


