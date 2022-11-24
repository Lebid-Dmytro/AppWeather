from django.core.paginator import Paginator
from django.db.models import QuerySet
from django.shortcuts import render
import requests
from django.views import generic, View
from django.views.generic import ListView

from .forms import CityForm
from .models import City


def sort_city():
    for row in City.objects.all():
        if City.objects.filter(name=row.name).count() > 1:
            row.delete()


def index(request):
    id = '20e10189b6ec3c7fb87ad17bb7a1bbe2'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + id

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.order_by('-id')[:5]

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
            'url': city.url,

        }
        all_cities.append(city_info)

    contex = {'all_info': all_cities, 'form': form, }

    sort_city()

    return render(request, 'weather/index.html', contex)


class CityInfo(View):
    def get(self, request, slug):
        # id_ten = '20e10189b6ec3c7fb87ad17bb7a1bbe2'
        # url_ten = 'https://api.openweathermap.org/data/2.5/forecast/daily?lat=44.34&lon=10.99&cnt=7&appid=' +id_ten
        city = City.objects.get(url=slug)

        contex = {'city': city, }
        return render(request, 'weather/about.html', contex)





