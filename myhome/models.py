from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20,)
    image = models.CharField( max_length=300,blank=True, null=True)
    author = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.CharField(max_length=1000)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post_id = models.CharField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

