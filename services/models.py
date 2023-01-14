from django.db import models
from froala_editor.fields import FroalaField
from django.utils.html import format_html

class ServiceTag(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class sfaq(models.Model):
    id = models.AutoField(primary_key=True)
    ftitle = models.CharField(max_length=150)
    ans = models.CharField(max_length=550)

    def __str__(self) -> str:
        return self.ftitle


class service(models.Model):
    id = models.AutoField(primary_key=True)
    tags = models.ManyToManyField(ServiceTag, blank=True)
    add_time = models.DateTimeField(auto_now_add=True, null=True)
    himage = models.ImageField(upload_to='portfoliothumb')
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=1000)
    shortdes = models.CharField(max_length=1000)
    fdes = FroalaField(max_length=1000)
    fimage = models.ImageField(upload_to='portfoliothumb')
    ffimage = models.ImageField(upload_to='portfoliothumb')
    ptitle1 = models.CharField(max_length=1000)
    pfdes1 = FroalaField(max_length=1000)
    ptitle2 = models.CharField(max_length=1000)
    pfdes2 = FroalaField(max_length=1000)
    ptitle3 = models.CharField(max_length=1000)
    pfdes3 = FroalaField(max_length=1000)
    ptitle4 = models.CharField(max_length=1000)
    pfdes4 = FroalaField(max_length=1000)
    mtitle = models.CharField(max_length=1000)
    mimage = models.ImageField(upload_to='portfoliothumb')
    mmimage = models.ImageField(upload_to='portfoliothumb')
    mdes = FroalaField(max_length=1000)
    faqtitle = models.CharField(max_length=1000)
    sfaq = models.ManyToManyField(
        sfaq,
        blank=True
    )
    url = models.SlugField(max_length=100)
    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:55px;height:70px" />'.format(self.himage))

    def __str__(self):
        return self.name