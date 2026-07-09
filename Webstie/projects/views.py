from django.shortcuts import render, get_object_or_404
from .models import Project, PersonalInfo

def project_list_view(request):
    all_projects = Project.objects.all()
    my_info = PersonalInfo.objects.first()
    context = {
        'projects': all_projects,
        'personal_info': my_info
    }
    return render(request, 'projects/project_list.html', context)

def project_detail_view(request, pk):
    single_project = get_object_or_404(Project, pk=pk)
    my_info = PersonalInfo.objects.first()
    context = {
        'project': single_project,
        'personal_info': my_info
    }
    return render(request, 'projects/project_detail.html', context)