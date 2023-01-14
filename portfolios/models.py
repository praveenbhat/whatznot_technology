from django.db import models
from froala_editor.fields import FroalaField
from django.utils.html import format_html

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.title

class portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    tags = models.ManyToManyField(
        Tag,
        blank=True
    )
    add_time = models.DateTimeField(auto_now_add=True, null=True)
    d_time = models.DateTimeField()
    type = models.CharField(max_length=1000)
    client = models.CharField(max_length=1000)
    himage = models.ImageField(upload_to='portfoliothumb')
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=1000)
    fdes = FroalaField(max_length=1000)
    vtitle = models.CharField(max_length=1000)
    vdes = FroalaField(max_length=1000)
    fontname = models.CharField(max_length=100)
    textsize = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    totalpages = models.CharField(max_length=100)
    bimage = models.ImageField(upload_to='bimage')
    simage = models.ImageField(upload_to='simage')
    ssimage = models.ImageField(upload_to='simage')
    mimage = models.ImageField(upload_to='simage')
    sssimage = models.ImageField(upload_to='simage')
    ssssimage = models.ImageField(upload_to='simage')
    lastcontent = FroalaField(max_length=1000)
    url = models.SlugField(max_length=100)

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:55px;height:70px" />'.format(self.himage))

    def __str__(self):
        return self.name