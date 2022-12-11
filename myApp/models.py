from turtle import title
from django.db import models

class Carousel(models.Model):
    title = models.CharField(max_length=200)
    paragraph = models.TextField(blank=True)
    
class Section(models.Model):
    title = models.CharField(max_length=200)
    paragraph = models.TextField(blank=True)
    
class Services(models.Model):
    title = models.CharField(max_length=200)
    paragraph = models.TextField(blank=True)
    image = models.ImageField( upload_to = "images/", null=True, blank=True)

class NewsUrl(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    paragraph = models.TextField(blank=True)
    image = models.ImageField( upload_to = "images/", null=True, blank=True)