from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Card, EmailStore


def index(request):
    return render(request, 'motivation.html')


def add_email(request):
    if request.method == "POST":
        email = request.POST.get('email')
    
        if email_valid(email):
            if not EmailStore.objects.filter(email=email).exists():
                email_store = EmailStore.objects.create(email=email)
                email_store.save()
                messages.success(request, "Wohooo ! Thanks for joining")
                return redirect('main:home')
            
            else:
                messages.success(request, "Already exists")
                return redirect('main:home')
        
        messages.success(request, "Invalid gmail address")
        return redirect('main:home')
        

    return render(request, 'motivation.html')

def email_valid(email_add):
    """checking email ends with @gmail.com"""

    if not str(email_add).endswith('@gmail.com'):
        return False
    
    elif not str(email_add).split('@')[0].islower():
        return False
    
    return True