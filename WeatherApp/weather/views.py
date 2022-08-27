from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'weather/index.html')


def new(request):
    return render(request, 'weather/new.html')