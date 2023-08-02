from django.db import models
from django.utils import timezone


class User(models.Model):
    class Meta:
        db_table = 'user'
    username = models.CharField(max_length=50, unique=True)
    # password = models.CharField(max_length=128, password=True)  ## no need auth now
    nickname = models.CharField(max_length=50)

    def __str__(self):
        return self.nickname


class Post(models.Model):
    class Meta:
        db_table = 'post'
    title = models.CharField(max_length=250)
    content = models.TextField(null=False, blank=False)
    # image_url = models.CharField() # for future
    # category = models.CharField() # for future
    view = models.IntegerField(default=0, null=True, blank=True)
    like = models.IntegerField(default=0, null=True, blank=True)
    dislike = models.IntegerField(default=0, null=True, blank=True)
    author = models.ForeignKey(User, related_name='author', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    class Meta:
        db_table = 'comment'
    user = models.ForeignKey(User, related_name='user', on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)
    like = models.IntegerField(default=0, null=True, blank=True)
    dislike = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

