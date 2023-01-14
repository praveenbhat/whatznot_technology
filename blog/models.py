from django.db import models
from froala_editor.fields import FroalaField
from django.utils.html import format_html
# from about.models import team_detail

class cat(models.Model):
    id = models.AutoField(primary_key=True)
    add_time = models.DateTimeField(auto_now_add=True, null=True)
    cat_name = models.CharField(max_length=100)

    def __str__(self):
        return self.cat_name

class author(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100)
    authorImage = models.ImageField(upload_to='author')

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:55px;height:70px" />'.format(self.authorImage))

    def __str__(self):
        return self.author
class blog(models.Model):
    id = models.AutoField(primary_key=True)
    add_time = models.DateTimeField(auto_now_add=True, null=True)
#    team_detail = models.ForeignKey(team_detail, on_delete=models.CASCADE,  null=True,)
    author = models.ForeignKey(author, on_delete=models.CASCADE,  null=True)
    category = models.ForeignKey(cat, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    content = FroalaField(max_length=1000)
    thumbimage = models.ImageField(upload_to='blogthumb')
    blogimage = models.ImageField(upload_to='blog')
    url = models.SlugField(max_length=100)

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:55px;height:70px" />'.format(self.thumbimage))

    def __str__(self):
        return self.title