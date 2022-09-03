from django.shortcuts import render
import requests


def index(request):
    appid = 'bb7dc3d70ae900cd335cdd42c1de4025'

    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    city = 'Minsk'
    res = requests.get(url.format(city)).json()

    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon'],
    }

    context = {'info': city_info}
    return render(request, 'weather/index.html', context)


def new(request):
    return render(request, 'weather/new.html')