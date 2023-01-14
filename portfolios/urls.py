from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', portfolios, name='portfolios'),
    path('<slug:url>/', portfolios_details, name='portfolio-details'),
]