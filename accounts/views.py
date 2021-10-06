from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from contacts.models import Contact

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already registered!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        first_name=first_name, 
                        last_name=last_name, 
                        username=username, 
                        email=email, 
                        password=password
                    )
                    user.save()
                    messages.success(request, 'You are now registered and can Log In')
                    return redirect('login')
        else:
            messages.error(request, 'Password and Confirm Password fields do not match!')
            return redirect('register')

    return render(request, 'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are successfully logged out')
        return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    user_inquiries = Contact.objects.order_by('-create_date').filter(user_id=request.user.id)
    context = {
        'inquiries': user_inquiries
    }
    return render(request, 'accounts/dashboard.html', context=context)