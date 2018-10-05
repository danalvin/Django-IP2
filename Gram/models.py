from django.db import models
from django.contrib.auth.models import User
import datetime as dt




class Image(models.Model):
    '''
    Image model
    '''
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=30, blank=True)
    image_caption = models.TextField(max_length=100, blank=True)
    user = models.ForeignKey(User, related_name="posted_by", on_delete=models.CASCADE, null=True)
    liker = models.ForeignKey(User, related_name='liked_by', on_delete=models.CASCADE, null=True)
    post_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.image_name

    @classmethod
    def get_all(cls):
        images = cls.objects.all()
        return images


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profile_pictures/')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=200, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, blank=True)
    following = models.ManyToManyField(User, related_name="follows", blank=True)
    followers = models.ManyToManyField(User, related_name="followed_by", blank=True)

    def __str__(self):
        return self.user.username

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles

class Comment(models.Model):
    content = models.TextField(max_length=150)
    user = models.ForeignKey(User, related_name='commented_by', on_delete=models.CASCADE)
    image = models.ForeignKey(Image, related_name='comment_for', on_delete=models.CASCADE)

    def __str__(self):  
        return self.content

    @classmethod
    def get_comments(cls):
        comments = cls.objects.all()
        return comments

class Likes(models.Model):
    likes = models.IntegerField()
    image = models.ForeignKey(Image, related_name='likes_for', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, related_name='who_is_liking', on_delete=models.CASCADE, null=True)



    def __str__(self):
        return str(self.likes)


