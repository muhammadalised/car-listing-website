from django.shortcuts import render

from cars import models
from .models import Team
from cars.models import Car

def home(request):
    team = Team.objects.all()
    featured_cars = Car.objects.order_by("-created_date").filter(is_featured=True)
    cars = Car.objects.order_by("-created_date")
    
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()


    context = {
        'page': 'home',
        'team': team,
        'featured_cars': featured_cars,
        'cars': cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
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

