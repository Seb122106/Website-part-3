from django.urls import path
from . import views

urlpatterns = [
    path('', views.TestimonyListView.as_view(), name='testimony_list'),
    path('add/', views.testimony_create, name='testimony_create'),
    path('<int:pk>/', views.testimony_detail, name='testimony_detail'),
]