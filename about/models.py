from django.db import models
from froala_editor.fields import FroalaField
from django.utils.html import format_html


class team_detail(models.Model):
    id = models.AutoField(primary_key=True)
    add_time = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    content = FroalaField(max_length=1000)
    image = models.ImageField(upload_to='team')
    facebook = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    freelancer = models.CharField(max_length=100)
    upwork = models.CharField(max_length=100)
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:55px;height:70px" />'.format(self.image))
