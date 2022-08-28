from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    appid = 'bb7dc3d70ae900cd335cdd42c1de4025'

    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    city = 'Minsk'
    res = requests.get(url.format(city))
    print(res.text)

    return render(request, 'weather/index.html')


def new(request):
    return render(request, 'weather/new.html')