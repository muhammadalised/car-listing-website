from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages

from .models import Team
from cars.models import Car

import os


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
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have a new message from Carzone website regarding '+ subject
        message_body = f'Name: {name}. Email: {email}. Phone: {phone}. Message:{message}.'

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        # Send the email to admin
        send_mail(
            email_subject,
            message_body,
            os.environ.get('EMAIL_HOST_USER'),
            [admin_email],
            fail_silently=False,
        )

        messages.success(request, 'Thank you for contacting us, we will get back to you shortly')
        return redirect('contact')
    
    return render(request, 'pages/contact.html', context=context)

