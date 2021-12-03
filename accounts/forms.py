from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import *
from django.forms import ModelForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email','phone',) # here we can other fields also according to uor need

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = '__all__'
class customerForm(forms.ModelForm):
    class Meta:
        model = customer
        fields="__all__"
class sellerForm(forms.ModelForm):
    class Meta:
        model = serviceProvider
        fields = '__all__'





