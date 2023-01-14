from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('faq/', faq, name='faq'),
    path('career/', career, name='career'),
    path('career/<slug:url>/', career_details, name='career-details'),


]

