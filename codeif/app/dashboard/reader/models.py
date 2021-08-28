from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User,AbstractUser
from app.user.models import CustomUser
from django.contrib.auth.models import AbstractUser


class readerDetails(models.Model):
  User_Name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default= 0)
  followings = models.IntegerField(default = 0)
  followingList = models.ManyToManyField(CustomUser, related_name='followingList')
  isValidated = models.BooleanField(default = False)
def __str__(self):
  return self.User_Name

class Followers(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    another_user = models.ManyToManyField(CustomUser, related_name='another_user')