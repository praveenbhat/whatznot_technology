from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', about, name='about'),
    path('team/', team, name='team'),
    path('team/<slug:url>/', team_details, name='team-details'),

]

