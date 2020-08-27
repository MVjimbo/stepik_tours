from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views import View


def custom_handler404(request, exception):
    return HttpResponseNotFound("Не получилось.404")


def custom_handler505(request):
    return HttpResponseNotFound("Не вышло.500")


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class DepartureView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'departure.html')


class TourView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tour.html')
