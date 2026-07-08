from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from projects.models import Project, PersonalInfo
def homepage(request):
    all_projects = Project.objects.all()
    my_info = PersonalInfo.objects.first()
    context = {
        'projects': all_projects,
        'personal_info': my_info
    }
    
    return render(request, 'home.html', context)

def aboutpage(request):
    return render(request, 'about.html')

def contactpage(request):
    return render(request, 'contact.html')

def skillsetpage(request):
    return render(request, 'skills.html')