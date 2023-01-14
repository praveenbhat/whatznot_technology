from django.contrib import admin
from .models import *

# Register your models here.


class FaqAdmin(admin.ModelAdmin):
    list_display = ( 'title',)
    search_fields = ( 'title',)
    list_per_page = 10


admin.site.register(faqs, FaqAdmin)

admin.site.register(Career)


