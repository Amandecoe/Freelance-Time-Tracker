from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.db.models import Q


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
    except Project.DoesnotExist():
        return Response("Project Doesn't Exist")  #checks if the project exists and continues if it does but doesn't continue if the project doesn't exist
    
    updated_project = ProjectSerializer(project, data=request.data)
    if updated_project.is_valid(): #checks if the updated project consists of all the required fields of a project
        updated_project.save()
        return Response("Project Updated Successfuly", updated_project.data)
    return Response("Required fields not filled") #if the updated project is missing some fields or is not valid

@api_view(['GET'])
def project_search(request):
    query = request.query_params.get("query")
    if not query:
        return Response("Nothing Found Under That Name")
    
    projects = Project.objects.filter(Q(name__iscontains=query) | Q(description__iscontains=query)) #Q is a django built in feature that allows you to search
    searched_product = ProjectSerializer(projects, many = True) #can return many products that match the result
    return Response(searched_product.data)

@api_view(['DELETE'])
def project_delete(request, pk):
    deleted_project = Project.objects.get(id = pk)
    deleted_project.delete()
