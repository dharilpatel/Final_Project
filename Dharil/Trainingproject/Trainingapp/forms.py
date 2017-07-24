from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):

    class Meta:
        model= User
        fields = ('first_name','last_name','username','password','email')