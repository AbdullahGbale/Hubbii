from django import forms
from .models import Project, Comment
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.db import models
from django.contrib.auth.models import User
from .models import PIP



class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'tags', 'demo_link', 'source_code_link', 'image', 'video']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),  # Adjust number of rows as needed
            'tags': forms.TextInput(attrs={'placeholder': 'e.g., Python, Django, Web Development'}),
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']





class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Use forms.EmailField instead of models.EmailField

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            UserProfile.objects.create(user=user)  # Create the related UserProfile instance
        return user
    




class PIPForm(forms.ModelForm):
    class Meta:
        model = PIP
        fields = ['title', 'summary', 'experience', 'education', 'skills', 'projects']
        widgets = {
            'summary': forms.Textarea(attrs={'rows': 4}),
            'experience': forms.Textarea(attrs={'rows': 4}),
            'education': forms.Textarea(attrs={'rows': 4}),
            'skills': forms.Textarea(attrs={'rows': 4}),
            'projects': forms.Textarea(attrs={'rows': 4}),
        }