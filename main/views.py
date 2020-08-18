from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'motivation.html')

def add_email(request):
    pass