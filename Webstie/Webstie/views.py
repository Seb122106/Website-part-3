from django.shortcuts import render
from projects.models import Project, PersonalInfo
from testimonies.models import Testimony


def homepage(request):
    context = {
        'projects': Project.objects.all(),
        'personal_info': PersonalInfo.objects.first(),
        'testimonies': Testimony.objects.order_by('-id')[:3],
    }
    return render(request, 'home.html', context)


def aboutpage(request):
    return render(request, 'about.html')


def contactpage(request):
    return render(request, 'contact.html')

def skillsetpage(request):
    return render(request, 'skills.html')