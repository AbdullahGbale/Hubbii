from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Portfolio, Certificate, Project, Post, Profile
from django.db import models

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



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio', 'twitter', 'linkedin', 'github']



class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'content']




class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        certificate_image = models.ImageField(upload_to='certificates/', blank=False)
        fields = ['title', 'certificate_image', 'description', 'issued_by', 'issue_date']  # Fields for the certificate form




class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'start_date', 'end_date', 'project_link', 'progress']