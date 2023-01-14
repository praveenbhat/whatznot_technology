from django.shortcuts import render
from .models import Contact


# Create your views here.


def contact(request):
    if request.method=="POST":
        con=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        sub=request.POST.get('sub')
        msg=request.POST.get('msg')
        con.name=name
        con.email=email
        con.phone=phone
        con.sub=sub
        con.msg=msg
        con.save()
        return render(request, 'home/home.html')

    return render(request, 'contact/contact.html')
