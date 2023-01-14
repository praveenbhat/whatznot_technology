from django.db import models
from froala_editor.fields import FroalaField
from django.utils.html import format_html



class faqs(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    des = FroalaField(max_length=1000)


    def __str__(self):
        return self.title


class Career(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True, blank=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    working_time = models.CharField(max_length=100)
    working_day = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    vacancy = models.CharField(max_length=100)
    content = FroalaField(max_length=5000)
    image = models.ImageField(upload_to='career')
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.name