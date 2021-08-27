from django.shortcuts import redirect, render
from .models import CustomUser
from django.contrib.auth import login,logout 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import SignupFORMS
from django.conf import settings
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

# Create your views here.

class UserRegisterView(generic.CreateView):
  form_class = SignupFORMS
  template_name  = 'registration/register.html'
  success_url = reverse_lazy('verify')

# class UserVerifyView():
#   form_class = SignupFORMS
#   template_name = 'registration/verify.html'
#   success_url = reverse_lazy('login')


def UserVerifyView(request):
  if request.method == 'POST':
    pass

  return render(request, 'registration/verify.html')

