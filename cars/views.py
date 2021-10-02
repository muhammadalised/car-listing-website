from django.core import paginator
from django.shortcuts import get_object_or_404, render
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from .models import Car

def cars(request):
    cars = Car.objects.order_by("-created_date")
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    context = {
        'page': 'cars',
        'cars': paged_cars
    }
    return render(request, 'cars/cars.html', context=context)

def car_details(request, id):
    car = get_object_or_404(Car, pk=id)
    print(type(car.features))
    context = {
        'car': car,
    }
    return render(request, 'cars/car-details.html', context=context)