from django.urls import path
from . import views

urlpatterns = [
 path('users/signup/', views.create_account, name = "create account"),
 path ('users/login/', views.login, name = "login page"),
 path ('users/logout/', views.logout, name = "Logout"),
]
