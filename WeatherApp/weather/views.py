from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index(request):
    appid = 'bb7dc3d70ae900cd335cdd42c1de4025'

    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()

    form = CityForm

    all_cities = []
    cities = City.objects.all()

    for city in cities:
        res = requests.get(url.format(city)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
        }
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}
    return render(request, 'weather/index.html', context)


def new(request):
    appid = 'bb7dc3d70ae900cd335cdd42c1de4025'

    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()

    form = CityForm

    all_cities = []
    cities = City.objects.all()

    for city in cities:
        res = requests.get(url.format(city)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
        }
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}
    return render(request, 'weather/new.html', context)
