from random import sample

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views import View

from data import tours, departures


def custom_handler404(request, exception):
    return HttpResponseNotFound("Не получилось.404")


def custom_handler505(request):
    return HttpResponseNotFound("Не вышло.500")


class MainView(View):
    def get(self, request):
        num_on_page = 6
        rand_tours_keys = sample(range(1, len(tours) + 1), num_on_page)
        rand_tours = {key: tours.get(key) for key in rand_tours_keys}
        context = {"tours": rand_tours}
        return render(request, 'index.html', context=context)


class DepartureView(View):
    def get(self, request, departure):
        count = 0
        min_price = 10000000
        max_price = 0
        min_nights = 10000000
        max_nights = 0
        specific_tours = []
        for key, tour in tours.items():
            if tour["departure"] == departure:
                if tour["price"] < min_price:
                    min_price = tour["price"]
                if tour["price"] > max_price:
                    max_price = tour["price"]

                if tour["nights"] < min_nights:
                    min_nights = tour["nights"]
                if tour["nights"] > max_nights:
                    max_nights = tour["nights"]
                count += 1
                specific_tours.append(tour)
                specific_tours[-1].update({"id": key})
        context = {
            "departure_title": departures[departure][3:],
            "count": count,
            "max_price": max_price,
            "min_price": min_price,
            "min_nights": min_nights,
            "max_nights": max_nights,
            "tours": specific_tours
        }
        return render(request, 'departure.html', context=context)


class TourView(View):
    def get(self, request, id, *args, **kwargs):
        tour = tours[id]
        departure = departures[tour["departure"]]
        context = {"tour": tour, "departure": departure[3:]}
        return render(request, 'tour.html', context=context)
