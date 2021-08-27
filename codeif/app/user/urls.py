from django.conf.urls.static import static
from django.urls import path
from .import views
from .views import *
from django.conf import settings


urlpatterns = [
  path('register', UserRegisterView.as_view(), name='register'),  
  path('verify', views.UserVerifyView, name='verify')
]