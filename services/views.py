from django.shortcuts import render
from .models import *
# Create your views here.


def services(request):
    serv = service.objects.all
    return render(request, 'service/service.html', {'serv': serv})


def service_details(request, url):
    ser = service.objects.get(url=url)
    return render(request, 'service/service-details.html', {'ser': ser})


