from django.shortcuts import render
from django.shortcuts import render
from .models import Freelancer
from .serializers import FreelancerSerializer
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['POST'])
def create_account(request):
    user = Freelancer.object.filter(request.user)
    serializer = FreelancerSerializer(user)
