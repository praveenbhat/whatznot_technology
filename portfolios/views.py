from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# Create your views here.


def portfolios(request):
    port = portfolio.objects.all()

    return render(request, 'portfolio/portfolio.html', {'port': port})


def portfolios_details(request, url):
    ports = portfolio.objects.get(url=url)

    return render(request, 'portfolio/portfolio-details.html', {'ports': ports,})






