from django.shortcuts import render
from .models import *
# Create your views here.


def about(request):
    team_list = team_detail.objects.all()
    return render(request, 'about/about.html', {'team_list': team_list})


def team(request):
    team_list = team_detail.objects.all()
    return render(request, 'about/team.html', {'team_list': team_list})



def team_details (request, url):
    team_detailss = team_detail.objects.get(url=url)
    return render(request, 'about/team-details.html', {'team_detailss': team_detailss })


