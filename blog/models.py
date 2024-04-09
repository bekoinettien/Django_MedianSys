from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    titre = models.CharField(max_length=50)
    slug =models.SlugField()

class ArticleBlog(models.Model):
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    titre = models.CharField(max_length=100)
    slug = models.SlugField()
    plublication = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    content =models.TextField()
    description = models.TextField()

class ArticleMedian(models.Model):
    titre = models.CharField(max_length=100)
    Datepub = models.DateField(blank=True)
    prix = models.FloatField()
    image = models.FileField()

