from django.shortcuts import render
from about.models import *
from .models import *
from blog.models import *
from portfolios.models import *
from services.models import *


# Create your views here.


def home(request):
    team_list = team_detail.objects.all()
    blo = blog.objects.all()[:2]
    faq = faqs.objects.all()[0:1]
    faaq = faqs.objects.all()[1:100]
    port = portfolio.objects.all()
    sa = service.objects.all()
    return render(request, 'home/home.html', {'team_list': team_list, 'blo': blo,'faq': faq, 'faaq': faaq, 'port': port, 'sa': sa, })


def faq(request):
    faq = faqs.objects.all()[0:1]
    faaq = faqs.objects.all()[1:100]
    return render(request, 'home/faq.html', {'faq': faq, 'faaq': faaq})


def career(request):
    car = Career.objects.all()
    return render(request, 'home/career.html', {'car': car})


def career_details(request, url):
    ca = Career.objects.get(url=url)
    return render(request, 'home/career-details.html', {'ca': ca})


