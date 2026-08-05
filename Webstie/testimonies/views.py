from django.shortcuts import render, redirect, get_object_or_404
from .models import Testimony
from .forms import TestimonyForm

def testimony_list_view(request):
    testimonies = Testimony.objects.all().order_by('-created_at')
    return render(request, 'testimonies/testimony_list.html', {'testimonies': testimonies})

def testimony_create_view(request):
    if request.method == 'POST':
        form = TestimonyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimony_list')
    else:
        form = TestimonyForm()
    return render(request, 'testimonies/testimony_form.html', {'form': form})

def testimony_detail_view(request, pk):
    testimony = get_object_or_404(Testimony, pk=pk)
    return render(request, 'testimonies/testimony_detail.html', {'testimony': testimony})