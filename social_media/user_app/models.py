from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    content = models.TextField(blank= True , null= True)
    image = models.ImageField(upload_to='post_images/' , blank= True , null= True)
    author = models.ForeignKey()

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    posts = models.ForeignKey()
# Create your models here.
