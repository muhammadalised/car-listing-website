from django.shortcuts import get_object_or_404, render
from .models import Car

def cars(request):
    cars = Car.objects.order_by("-created_date")
    context = {
        'page': 'cars',
        'cars': cars
    }
    return render(request, 'cars/cars.html', context=context)

def car_details(request, id):
    car = get_object_or_404(Car, pk=id)
    print(type(car.features))
    context = {
        'car': car,
    }
    return render(request, 'cars/car-details.html', context=context)