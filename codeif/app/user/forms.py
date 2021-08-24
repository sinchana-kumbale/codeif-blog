from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import CustomUser


CHOICES= [
  ('Writer', 'Writer'),
  ('Reader', 'Reader'),
]

# sign-up form based class based view 
class SignupFORMS(UserCreationForm):

  name = forms.CharField(max_length=500,
    widget=forms.TextInput(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))

  Category= forms.CharField(label='What is your are?', widget=forms.RadioSelect(choices=CHOICES))

  #For Attribute ordering
  class Meta:
    model = CustomUser
    fields = ('name','email','Category','password1','password2')

  #For user-name and password designing
  def __init__(self, *args, **kwargs):
    super(SignupFORMS,self).__init__(*args, **kwargs)

  