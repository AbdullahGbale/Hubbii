from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Profile Model to extend User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="main_profile")
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='default.jpg')

    def __str__(self):
        return self.user.username

# Project Model
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Certificate Model
class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issued_by = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificates')
    date_issued = models.DateField()

    def __str__(self):
        return self.title

# Portfolio Model
class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.TextField()
    experience = models.TextField()
    projects = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s Portfolio"

