from django.db import models
from django.contrib.auth.models import User


# Extend User with Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pictures/", default="default.jpg")
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    github = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username


# Project Model
class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Post Model
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=255)
    content = models.TextField()
    skills = models.CharField(max_length=255, blank=True, null=True)
    technologies = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="portfolio_posts/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.user.username}"


# Comment Model
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"


# Rating Model
class Rating(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 8)])

    def __str__(self):
        return f"{self.stars} stars for {self.project.title} by {self.user.username}"


# Compliment Model
class Compliment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="compliments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"Compliment by {self.user.username}"


# Collaboration Request Model
class CollaborationRequest(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="collaborations")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_collaborations")
    status = models.CharField(
        max_length=20,
        choices=[("Pending", "Pending"), ("Accepted", "Accepted"), ("Declined", "Declined")],
        default="Pending",
    )

    def __str__(self):
        return f"Request by {self.sender.username} for {self.project.title}"


# Reaction Model
class Reaction(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="reactions")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    emoji = models.CharField(max_length=10)

    def __str__(self):
        return f"Reaction by {self.user.username}"


# Collaboration Request for Profiles
class CollaboRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_collabo_requests")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_collabo_requests")
    status = models.CharField(
        max_length=20,
        choices=[("Pending", "Pending"), ("Accepted", "Accepted"), ("Declined", "Declined")],
        default="Pending",
    )

    def __str__(self):
        return f"Collabo Request: {self.sender.username} -> {self.receiver.username}"


# Amp Model
class Amp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="amps")
    target_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="amped_by")

    def __str__(self):
        return f"{self.user.username} amped {self.target_user.username}"
