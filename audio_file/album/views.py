from django.http import HttpResponse
from album.models import AlbumData,Songs_list
from django.shortcuts import render

def check(request):
    return HttpResponse("<a href='http://127.0.0.1:8000/list/'><button>Album List</button></a>")

def ablum_list(request):
    data = AlbumData.objects.all()
    myAlbumDict = {
        "albums":data
    }
    return render(request,"album_list.html",myAlbumDict)

def song_list(request,target):
    alb = AlbumData.objects.get(id = target)
    alb_data = Songs_list.objects.filter(album = alb)
    mySongList = {
        "alb":alb,
    }
    if alb_data:
        mySongList["songs"] = alb_data
    return render(request,"album_data.html",mySongList)


