from django import forms
from django.contrib.auth.forms import UserCreationForm #built-in form that already handles
# password hashing, validation, and checking that passwords match.
#handles checking password1 vs password2 by itself.
from django.contrib.auth.models import User
from .models import Freelancer

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True) #adds an email field to the form, making it required
    class Meta:
        model = User #This form saves to the User model in the database
        fields = ['username', 'email', 'password1', 'password2'] #defines which fields the form will display

class ProfileForm(forms.ModelForm): # a standard model form tied to our Freelancer model
    class Meta:
        model = Freelancer #which model to save to
        fields = {"bio"}
