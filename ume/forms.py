from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from ume.models import *
from django.forms import ModelForm
from django import forms

class ServiceProviderPost(forms.ModelForm):
    class Meta:
        model= sellerPost
        fields = ('title','description','image','price','tags')