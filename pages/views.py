from django.shortcuts import render
from .models import Team

def home(request):
    team = Team.objects.all()
    context = {
        'page': 'home',
        'team': team,
    }
    return render(request, 'pages/home.html', context=context)

def about(request):
    team = Team.objects.all()
    context = {
        'page': 'about',
        'team': team,
    }
    return render(request, 'pages/about.html', context=context)

def services(request):
    context = {
        'page': 'services'
    }
    return render(request, 'pages/services.html', context=context)

def contact(request):
    context = {'page': 'contact'}
    return render(request, 'pages/contact.html', context=context)

