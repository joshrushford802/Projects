from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    calender_date = models.DateTimeField(auto_now_add=True)
    maker = models.ForeignKey(User, related_name='creator', on_delete=models.CASCADE, null=True)
    material = models.CharField(max_length=300, null=True)


class Like(models.Model):
    pid = models.ForeignKey(Post, related_name='post_id_like', on_delete=models.CASCADE)
    dweller = models.ForeignKey(User, related_name='owner_like', on_delete=models.CASCADE)


class Follow(models.Model):
    sub = models.ForeignKey(User, related_name='sub', on_delete=models.CASCADE)
    dweller = models.ForeignKey(User, related_name='dweller', on_delete=models.CASCADE)