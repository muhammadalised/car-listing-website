from django.shortcuts import render
from .models import Team

def home(request):
    team = Team.objects.all()
    context = {
        'team': team,
    }
    return render(request, 'pages/home.html', context=context)

def about(request):
    team = Team.objects.all()
    context = {
        'team': team,
    }
    return render(request, 'pages/about.html', context=context)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')

