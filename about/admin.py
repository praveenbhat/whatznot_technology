from django.contrib import admin
from .models import *

# Register your models here.



class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'job', 'image_tag', 'url', 'add_time')
    search_fields = ('name', 'job')
    list_per_page = 3

#  Register your models here.
admin.site.register(team_detail, MemberAdmin)



