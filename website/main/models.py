from django.db import models
from django.contrib.auth.models import User



class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=255, blank=True, help_text="Separate tags with commas")
    demo_link = models.URLField(blank=True)
    source_code_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    video = models.FileField(upload_to='project_videos/', blank=True, null=True)

    likes = models.ManyToManyField(User, related_name='liked_projects', blank=True)

    total_rating = models.IntegerField(default=0)
    num_ratings = models.IntegerField(default=0)

    def total_likes(self):
        return self.likes.count()

    def average_rating(self):
        if self.num_ratings == 0:
            return 0
        return self.total_rating / self.num_ratings

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', args=[self.id])
    

    

class Rating(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 8)])  # 1 to 7

    class Meta:
        unique_together = ('project', 'user') # One rating per user per project




class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)






class CollaborationRequest(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='collaboration_requests')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_collaboration_requests')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_collaboration_requests')
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)




class Reaction(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reactions')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reaction_type = models.CharField(max_length=20, choices=[
        ('like', 'Like'),
        ('love', 'Love'),
        ('wow', 'Wow'),
        ('haha', 'Haha'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
    ])

    class Meta:
        unique_together = ('project', 'user', 'reaction_type')




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True)
    # Add other profile fields as needed



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return self.user.username




class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    video = models.FileField(upload_to='post_videos/', blank=True, null=True)
    audio = models.FileField(upload_to='post_audio/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user.username} on {self.created_at}"
    



class PIP(models.Model):  # Portfolio Interview Post
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    summary = models.TextField()
    experience = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    projects = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at'] # Order by latest post
