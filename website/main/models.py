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



'''
# Project Model
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
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
    






# Third portfolio model
class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
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
    







class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Rating(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 8)])



class Compliment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='compliments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()




class CollaborationRequest(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='collaborations')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Declined', 'Declined')])




class Reaction(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reactions')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    emoji = models.CharField(max_length=10)




class TeamMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='team_members')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    is_accepted = models.BooleanField(default=False)





class CollaboRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_collabos')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_collabos')
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Declined', 'Declined')])
 

 
class Amp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='amps')
    target_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='amped_by')
