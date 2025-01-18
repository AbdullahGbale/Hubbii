from django import forms
from .models import Project, Comment

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']