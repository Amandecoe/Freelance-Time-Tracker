from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()

@api_view(['GET'])
def List_Projects(request):
    project = Project.object.filter(user = request.user)
    serialzier = ProjectSerializer(project)
    return Response(serialzier.data)

@api_view(['POST'])
def add_project(request):
   name = request.data.get("name")
   description = request.data.get("description")
   newproject = ProjectSerializer(data=request.data) #accepts all the data sent by the user to create a new project
   if newproject.is_valid(): #checks if all the input data from the user matches the one's required to create a new project
       newproject.save() #saves the new project
       return Response(newproject.data, "Project created")
   if Project.objects.filter(name=name,description=description).exists():
       return Response("Project already exists")    
   
@api_view(['PUT'])
def update_project(request,pk):
    try:
        project = Project.objects.get(pk = pk)
    except: Project.DoesnotExist:
        return Response("Project Doesn't Exist")
    serializer = ProjectSerializer(project, data=request.data)
    if serializer.is_valid():
