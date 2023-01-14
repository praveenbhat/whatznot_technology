from django.contrib import admin
from .models import Contact



class contactAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'phone', 'email', 'sub', 'time')
    search_fields = ( 'name', 'phone', 'email', 'sub',)
    list_per_page = 10

admin.site.register(Contact, contactAdmin)