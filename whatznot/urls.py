
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('portfolio/', include('portfolios.urls')),
    path('service/', include('services.urls')),




]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
