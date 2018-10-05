from django.db import models
from django.contrib.auth.models import User
import datetime as dt


# Create your models here.
 
class image(models.Model):
    image = models.ImageField(upload_to='image/')
    image_name = models.CharField(max_length=30, blank=True)
    image_caption = models.TextField(max_length=90, blank=True)
    user = models.ForeignKey(User, related_name="posted_by", on_delete=models.CASCADE, null=True)
    liker = models.ForeignKey(User, related_name="liked_by", on_delete=models.CASCADE, null=True)
    post_date = models.DateTimeField(auto_now=True)
    
class profile(models.Model):
    profile_picture = models.ImageField(upload_to='image/')
    bio = models.TextField(max_length=30, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    followers = models.ManyToManyField(User, related_name="followed_by", blank=True)
    following = models.ManyToManyField(User, related_name="follows", blank=True)


class user(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=150) 

