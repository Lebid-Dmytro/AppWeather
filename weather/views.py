from django.shortcuts import render
import requests
from django.views.generic import ListView

from .forms import CityForm
from .models import City


def sort_city():
    cities = City.objects.all()
    new_list = dict()
    for i in cities:
        if i == new_list:
            cities.clear(i)
    return new_list


def index(request):
    id = '20e10189b6ec3c7fb87ad17bb7a1bbe2'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + id

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()[:5]

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']

        }
        all_cities.append(city_info)

    contex = {'all_info': all_cities, 'form': form}
    sort_city()
    return render(request, 'weather/index.html', contex)


# class WeathersView(About, ListView):
#     def get(self, request):
#         abouts = About.objects.all()
#         return render(request, 'weather/index.html', {'all_app': abouts})
# def about(request):
#     id = '20e10189b6ec3c7fb87ad17bb7a1bbe2'
#     url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + id
#
#     # app = About.objects.all()
#
#     cities = About.objects.all()
#     all_cit = []
#
#     for city in cities:
#         rest = requests.get(url.format(city.name)).json()
#         city_inf = {
#             'city': city.name,
#             'temp': rest['main']['temp']
#         }
#
#         all_cit.append(city_inf)
#
#     tex = {'info_cit': city_inf}
#
#     return render(request, 'weather/about.html', tex)
def about(request):
    id = '20e10189b6ec3c7fb87ad17bb7a1bbe2'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + id


    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = About.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']

        }
        all_cities.append(city_info)

    contex = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/about.html', contex)