from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Portfolio, Certificate, Project, Post, Profile, Comment


class CustomSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserSearchForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, label="Search for a user")




class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio', 'twitter', 'linkedin', 'github']


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['skills', 'your_DP_image', 'about_you', 'project_link']


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['title', 'certificate_image', 'description', 'issued_by', 'issue_date']







class ProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = ['title', 'image',  'description', 'start_date', 'end_date', 'project_link', 'progress', 'technologies']





class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'skills', 'technologies', 'image']




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']