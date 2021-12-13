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
# class customerForm(forms.ModelForm):
#     class Meta:
#         model = customer
#         fields="__all__"
# class sellerForm(forms.ModelForm):
#     class Meta:
#         model = serviceProvider
#         fields = '__all__'

class BuyerForm(UserCreationForm):
    class Meta:
        model = customer
        fields= ('email','phone',)

class SellerForm(UserCreationForm):
    class Meta:
        model = ServiceProvider
        fields= ('email','phone',)

class sellerSignupForm(forms.ModelForm):
    # first_name = forms.CharField(max_length=20)
    # last_name =  forms.CharField(max_length=20)
    # your_Address = forms.CharField(max_length=150)
    class Meta:
        model = serviceProviderDetails
        fields = ('first_name','last_name','your_Address')

