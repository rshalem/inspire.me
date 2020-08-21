from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .models import Card, EmailStore


def index(request):
    quotes = Card.objects.all()
    paginator = Paginator(quotes, 6)
    
    # getting the requested page number
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'motivation.html', context)


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
