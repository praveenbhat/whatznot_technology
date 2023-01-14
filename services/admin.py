from django.contrib import admin
from .models import *






admin.site.register(ServiceTag)

admin.site.register(sfaq)

class serviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag', 'title')
    search_fields = ('name', 'title')
    list_per_page = 10

admin.site.register(service, serviceAdmin)