from django.db import models
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User,AbstractUser
from app.user.models import CustomUser
from django.contrib.auth.models import AbstractUser

# Create your models here.
class writerDetails(models.Model):
  User_Name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default= 0)
  User_Name_Trial = models.CharField(max_length = 200,default = "",blank = True)
  follower = models.IntegerField(default = 0)
  followerList = models.ManyToManyField(CustomUser, related_name='followerList')
  isValidated = models.BooleanField(default = False)
def __str__(self):
  return self.User_Name




