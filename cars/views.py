from django.shortcuts import render

def cars(request):
    context = {
        'page': 'cars',
    }
    return render(request, 'cars/cars.html', context=context)