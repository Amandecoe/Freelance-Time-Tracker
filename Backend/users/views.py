from django.shortcuts import render
from django.shortcuts import render
from .models import Freelancer
from .serializers import FreelancerSerializer
from rest_framework.decorators import api_view
from .forms import UserRegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
import json
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


@api_view(['POST'])
def login(request):
    data = json.loads(request.body) #contains the raw data from the client which is converted to python dictionary by json
    username = data["username"] #extracts the username from the JSON we just saved inside "data"
    password = data["password"] #extracts the password from the JSON we just saved inside "data"

    user = authenticate(request, username = username, password = password)
    #django looks up a user with that username, hashes the given password and then compares it to the one in the database
    if user is not None:
        login(request,user) #if authentication succeded it logs the user in
        return JsonResponse({"success": True, "message":"Logged in"}, status = 200)
    else:
        return JsonResponse({"success":False, "message":"Invalid Credentials"}, status = 401)

@api_view(['POST'])
def logout(request):
    logout(request) #doesn't need the user because it works by accessing the current user session's data that is created when user logged in
    return JsonResponse({"success":True, "message": "User have been Logged Out!"}, status=200)


