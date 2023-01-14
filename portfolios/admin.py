from django.contrib import admin
from .models import *



class portfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag', 'title')
    search_fields = ('name', 'title')
    list_per_page = 10

admin.site.register(portfolio, portfolioAdmin)




admin.site.register(Tag)