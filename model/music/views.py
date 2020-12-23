from django.shortcuts import render
from django.http import HttpResponse
from music.models import  songs
# Create your views here.

def data(request):
    album = songs.objects.all()
    html = "<h1>Your Datas are</h1>"
    for a in album:
        if a.status:
            html+= f"<li>{a.content}<li>"
    return HttpResponse(html)
