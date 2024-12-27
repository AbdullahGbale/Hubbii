
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
