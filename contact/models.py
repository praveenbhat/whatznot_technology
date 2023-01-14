from django.db import models

from django.utils.html import format_html


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    sub = models.CharField(max_length=1000)
    msg = models.TextField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name
