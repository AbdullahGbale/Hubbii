from django.db import models



# Define status choices
STATUS_CHOICES = [
    ('active', 'Active'),
    ('completed', 'Completed'),
    ('archived', 'Archived'),
]

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')  # Add status field
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name



class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    projects = models.ManyToManyField(Project)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')  # Add status field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

