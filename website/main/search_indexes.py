from haystack import indexes
from django.contrib.auth.models import User
from .models import Project

class UserIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)  # Use a template for indexing multiple fields
    username = indexes.CharField(model_attr='username')

    def get_model(self):
        return User

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class ProjectIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    description = indexes.CharField(model_attr='description')
    owner = indexes.CharField(model_attr='owner__username')

    def get_model(self):
        return Project

    def index_queryset(self, using=None):
        return self.get_model().objects.all()