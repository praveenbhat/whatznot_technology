from django.shortcuts import render
from .models import blog, cat, author

# Create your views here.



def blog_all (request):
    blogs = blog.objects.all()
    return render(request, 'blog/blog.html', {'blogs': blogs})


def blog_d (request, url):
    blogs = blog.objects.get(url=url)
    r = blog.objects.all()[:3]
    cats = cat.objects.all()
    aut = author.objects.all()
    return render(request, 'blog/blog-details.html', {'blogs': blogs, 'r': r , 'cats': cats, 'aut': aut })



