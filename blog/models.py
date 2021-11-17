from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    slug = models.CharField(max_length=130)

    def __str__(self):
        return self.title + 'by' + self.auther

class BlogComment(models.Model):
    sno = models.AutoField(primary_key= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    Parent = models.ForeignKey('self', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=now)