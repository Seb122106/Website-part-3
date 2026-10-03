from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from projects.models import Project, TechStack
from .forms import AdminLoginForm, ProjectForm, TechStackForm

superuser_required = user_passes_test(
    lambda user: user.is_active and user.is_superuser,
    login_url='dashboard_login',
)


class AdminLoginView(LoginView):
    authentication_form = AdminLoginForm
    template_name = 'dashboard/login.html'


@superuser_required
def dashboard_home(request):
    projects = Project.objects.prefetch_related('tech_stacks')
    return render(request, 'dashboard/project_table.html', {'projects': projects})


@superuser_required
def tech_stack_list(request):
    tech_stacks = TechStack.objects.prefetch_related('projects')
    return render(request, 'dashboard/techstack_table.html', {'tech_stacks': tech_stacks})


@superuser_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project added.')
            return redirect('dashboard_home')
    else:
        form = ProjectForm()
    return render(request, 'dashboard/project_form.html', {
        'form': form,
        'has_stacks': TechStack.objects.exists(),
    })


@superuser_required
def tech_stack_create(request):
    if request.method == 'POST':
        form = TechStackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tech stack added.')
            return redirect('dashboard_tech_stacks')
    else:
        form = TechStackForm()
    return render(request, 'dashboard/techstack_form.html', {'form': form})