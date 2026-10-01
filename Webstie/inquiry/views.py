from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Inquiry


def contact_view(request):
    if request.method == 'POST':
        Inquiry.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            contact_number=request.POST.get('contact_number'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            message=request.POST.get('message'),
        )
        messages.success(request, 'Thanks for reaching out! I will get back to you soon.')
        return redirect('contact')
    return render(request, 'contact.html')