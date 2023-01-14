from django.contrib import admin
from .models import *

# Register your models here.


class authoraAdmin(admin.ModelAdmin):
    list_display = ('author', 'image_tag')
    search_fields = ('author',)
    list_per_page = 10

admin.site.register(author, authoraAdmin)



class catAdmin(admin.ModelAdmin):
    list_display = ('cat_name','add_time')
    search_fields = ('cat_name',)
    list_per_page = 10


admin.site.register(cat, catAdmin)




class BlogAdmin(admin.ModelAdmin):
    list_display = ( 'author', 'image_tag', 'url', 'add_time','category')
    list_filter = ('author','category' )
    search_fields = ('author', 'job', 'title', 'content')
    list_per_page = 10


admin.site.register(blog, BlogAdmin)









