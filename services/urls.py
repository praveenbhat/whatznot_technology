from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', services, name='service'),
    path('<slug:url>/', service_details, name='service-details'),
]