from django.urls import path
from .views import testimony_list_view, testimony_create_view, testimony_detail_view

urlpatterns = [
    path('', testimony_list_view, name='testimony_list'),
    path('add/', testimony_create_view, name='testimony_add'),
    path('<int:pk>/', testimony_detail_view, name='testimony_detail'),
]