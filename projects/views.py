from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, PersonalInfo

def project_list_view(request):
    all_projects = Project.objects.prefetch_related('tech_stacks')
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

#WILL COMMENT NALANG AS IT IS REDUNDANT
# def project_create_view(request):
#     if request.method == 'POST':
#         form = ProjectForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('project_list')
     # else:
    #     form = ProjectForm()
    # return render(request, 'projects/project_form.html', {'form': form})