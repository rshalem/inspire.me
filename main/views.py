from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import JsonResponse

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
    """ajax post handling, data coming from frontend checked at backend
       & sent back as a JSON response 
    """

    email_value = request.POST.get('email_val', None)

    data = {}
    if not EmailStore.objects.filter(email=email_value).exists() and str(email_value).endswith('@gmail.com') and str(email_value).split('@')[0].islower():
        email_store = EmailStore.objects.create(email=email_value)
        email_store.save()
        data['status'] = True

    else:
        data['status'] = False

    return JsonResponse(data)



# def email_valid(email_add):
#     """checking email ends with @gmail.com"""

#     if not str(email_add).endswith('@gmail.com'):
#         return False
    
#     elif not str(email_add).split('@')[0].islower():
#         return False
    
#     return True

def email_validation(request):

    email_val = request.GET.get('entered_email', None)

    data = {}
    
    if EmailStore.objects.filter(email=email_val).exists():
        data['is_taken'] = True
        # data['email'] = email_val

    return JsonResponse(data)