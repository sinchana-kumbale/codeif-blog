from django import forms
from .models import post

class CpostFORMS(forms.Form):
  TitleF = forms.CharField(max_length=500,
    widget=forms.TextInput(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))

  DetailsF= forms.CharField(max_length=50000,
    widget= forms.Textarea(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))

  '''CategoryF= forms.ChoiceField(choices=choices, 
    widget= forms.Select(attrs={
      'class':'form-control',
      'id'   :'title',      
    }))'''


class UpostFORMS(forms.Form):
  TitleF = forms.CharField(max_length=500,
    widget=forms.TextInput(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))

  DetailsF= forms.CharField(max_length=50000,
    widget= forms.Textarea(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))

  '''CategoryF= forms.ChoiceField(choices=choices, 
    widget= forms.Select(attrs={
      'class':'form-control',
      'id'   :'title',      
    }))'''

   
  
  
