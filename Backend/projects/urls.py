from django.urls import path
from . import views

urlpatterns = [
    path("project/project_list/", views.List_Projects, name = "project_list"),
    path ("project/add_project/", views.add_project, name = "add_project"),
    path("project/update_project/<int:pk>/", views.update_project, name = "update_project"),
    path ("project/project_search/", views.project_search, name = "project_search"),
    path ("project/project_delete/<int:pk>/", views.project_delete, name = "project_delete")
]
