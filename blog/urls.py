from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', blog_all, name='blog'),
    path('<slug:url>/', blog_d, name='blog-details'),



]