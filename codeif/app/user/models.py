from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
  name = models.CharField(max_length=50)
  email = models.EmailField(max_length=100,unique=True)
  username = None
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []
  Category = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

