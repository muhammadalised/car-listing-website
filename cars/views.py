from django.core import paginator
from django.shortcuts import get_object_or_404, render
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from .models import Car

def cars(request):
    cars = Car.objects.order_by("-created_date")
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

    context = {
        'page': 'cars',
        'cars': paged_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'cars/cars.html', context=context)

def car_details(request, id):
    car = get_object_or_404(Car, pk=id)
    context = {
        'car': car,
    }
    return render(request, 'cars/car-details.html', context=context)

def search(request):
    cars = Car.objects.order_by("-created_date")

    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()


    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword')
        cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET.get('model')
        cars = cars.filter(model__iexact=model)

    
    if 'city' in request.GET:
        city = request.GET.get('city')
        cars = cars.filter(city__iexact=city)

    
    if 'year' in request.GET:
        year = request.GET.get('year')
        cars = cars.filter(year__iexact=year)
    
    
    if 'body-style' in request.GET:
        body_style = request.GET.get('body-style')
        cars = cars.filter(body_style__iexact=body_style)
    
    if 'transmission' in request.GET:
        transmission = request.GET.get('transmission')
        cars = cars.filter(transmission__iexact=transmission)

    if 'min_price' in request.GET:
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')

        cars = cars.filter(price__gte=min_price, price__lte=max_price)
        

    context = {
        'cars': cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'transmission_search': transmission_search,
    }
    return render(request, 'cars/search.html', context=context)