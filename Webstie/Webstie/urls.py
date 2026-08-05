from django.contrib import admin
from django.urls import include, path
from Webstie.views import aboutpage, homepage, skillsetpage
from projects import views as project_views
from inquiry import views as inquiry_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('about/', aboutpage, name='about'),
    path('contact/', inquiry_views.contact_view, name='contact'),
    path('skillset/', skillsetpage, name='skillset'),
    path('projects/', project_views.project_list_view, name='project_list'),
    path('project/<int:pk>/', project_views.project_detail_view, name='project_detail'),
    path('testimonies/', include('testimonies.urls')),
]