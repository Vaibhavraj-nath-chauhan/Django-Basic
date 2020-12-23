from django.shortcuts import render
from django.shortcuts import render
from Music.models import album
# Create your views here.
def html(request):
    data = album.objects.all()
    d = {
        "Name": "Swagat",
        "alb": data
    }
    return render(request,"learn.html",d)

def perticular(request,id):
    data = album.objects.filter(id = id)
    d = {
        "det":data
    }
    return render(request,"detail.html",d)
