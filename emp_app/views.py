from django.shortcuts import render
from .models import Employee, Role, Department

# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')
    

def feature(request):
    return render(request, 'feature.html')


def pricing(request):
    return render(request, 'pricing.html')

def banner(request):
    return render(request, 'banner.html')

def blog(request):
    return render(request, 'blog.html')

