from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.core.mail import send_mail

import os

from .models import Contact

def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_inquiry = request.POST['customer_inquiry']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already inquired about this car! Please wait until we get back to you shortly.')
                return redirect(f'/cars/{car_id}')

        contact = Contact(
            first_name = first_name,
            last_name = last_name,
            user_id = user_id,
            car_id = car_id,
            car_title = car_title,
            customer_inquiry = customer_inquiry,
            city = city,
            state = state,
            email = email,
            phone = phone,
            message = message
        )

        contact.save()
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        # Send the email to admin
        send_mail(
            f'Inquiry for {car_title}',
            f'You have an inquiry for the car {car_title}. Please login to your admin panel for more info.',
            os.environ.get('EMAIL_HOST_USER'),
            [admin_email],
            fail_silently=False,
        )

        messages.success(request, 'Your request has been received, we will get back to you shortly')
        return redirect(f'/cars/{car_id}')