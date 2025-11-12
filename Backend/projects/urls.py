from django.urls import path
from . import views

urlpatterns = [
    path("project_list/", views.List_Projects, name = "project_list"),
    path ("add_project/", views.add_project, name = "add_project"),
    path("update_project/<int:pk>/", views.update_project, name = "update_project"),
    path ("project_search/", views.project_search, name = "project_search"),
    path ("project_delete/<int:pk>/", views.project_delete, name = "project_delete")
]
