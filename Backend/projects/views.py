from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()
@api_view(["GET"])
def List_Project(request):
    project = Project.object.filter(user = request.user)
    serialzier = ProjectSerializer(project)
    return Response(serialzier.data)
