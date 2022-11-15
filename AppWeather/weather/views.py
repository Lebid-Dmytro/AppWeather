from django.core.paginator import Paginator
from django.db.models import QuerySet
from django.shortcuts import render
import requests
from django.views import generic
from django.views.generic import ListView

from .forms import CityForm
from .models import City


def sort_city():
    for row in City.objects.all():
        if City.objects.filter(name=row.name).count() > 1:
            row.delete()


def index(request):
    idt = '20e10189b6ec3c7fb87ad17bb7a1bbe2'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + idt

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    else:
        pass

    form = CityForm()

    cities = City.objects.order_by('id')

    all_cities = []

    paginator = Paginator(all_cities, 5)

    for city in cities[::-1]:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']

        }
        all_cities.append(city_info)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    contex = {'all_info': all_cities, 'form': form, 'page_obj': page_obj}

    sort_city()

    return render(request, 'weather/index.html', contex)


