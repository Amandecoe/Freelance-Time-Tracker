from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.response import Response
# Create your views here.

@api_view(["GET"])
def List_Project(request):
    project = Project.object.filter()
    serialzier = ProjectSerializer(Project)
    return Response(serialzier.data)
