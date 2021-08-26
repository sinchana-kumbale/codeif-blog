from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from app.user.models import CustomUser
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# POST creation 
class post(models.Model):
  User_Name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default= 0)
  Users_views = models.ManyToManyField(CustomUser, related_name='Users_views', default= 0)
  Category = models.CharField(max_length=100,null=True,primary_key=False)
  Title   = models.CharField(max_length=500, null=True,primary_key=False)
  Details = models.TextField()

  views = models.IntegerField(default=0)


  #views = models.IntegerField(max_length=200,default=0)

  published_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.Title

class Category(models.Model):
    name = models.CharField(max_length=255)     
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')