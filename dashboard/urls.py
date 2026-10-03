from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('tech-stacks/', views.tech_stack_list, name='dashboard_tech_stacks'),
    path('projects/add/', views.project_create, name='dashboard_project_create'),
    path('tech-stacks/add/', views.tech_stack_create, name='dashboard_tech_stack_create'),
    path('login/', views.AdminLoginView.as_view(), name='dashboard_login'),
    path('logout/', LogoutView.as_view(), name='dashboard_logout'),
]