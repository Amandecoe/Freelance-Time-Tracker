from django.db import models
from django.contrib.auth.models import User
from django.utils import slugify
# Create your models here.
#Django has a built in user model with firstname, lastname, email, password etc properties so we only need
# a field that relates that user to a freelancer account
class Freelancer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank = True)
    skills = models.TextField(blank=True)


