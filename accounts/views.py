from django.shortcuts import render

def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    return render(request, 'accounts/register.html')

def logout(request):
    return render(request, 'accounts/logout.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')