from django.shortcuts import render
from django.shortcuts import render
from .models import Freelancer
from .serializers import FreelancerSerializer
from rest_framework.decorators import api_view
from .forms import UserRegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@api_view(['POST']) #accepts POST requests
def create_account(request):
    user_form = UserRegisterForm(request.data)
    profile_form = ProfileForm(request.data) #these two contain all the input entered into the forms of the user register and profile register.
    if user_form.is_valid() and profile_form.is_valid(): #checks if the entered input is right, like if username is taken, passwords match etc on user_form
        user = user_form.save() #creates a new user in the database
        profile = profile_form.save(commit=False) #creates a profile instance but doesn't save it yet because of the commit=false
        # which allows us to attach the use to a profile before saving
        profile.user = user  #links the profile to a newly created user via the OnetoOneField
        profile.save() #saves the profile in the database





