from django.shortcuts import render, redirect
from Music.models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
# index page


def home(request):
    return render(request, "home.html")


# album list
def album(request):
    data = [i for i in Album.objects.all() if i.status]
    d = {
        "album": data,
    }
    return render(request, 'album_list.html', d)


# album data
def album_data(request, target):
    data = Album.objects.get(id=target)
    song = [i for i in Song.objects.filter(album=data) if i.status]
    d = {
        "album": data,
        'song': song,
    }
    return render(request, 'album_data.html', d)


# adding album from user foental
def add_album(request):
    if request.method == "POST":
        data = request.POST
        title = data["title"]
        banner = request.FILES["banner"]
        status = data["PU"]
        if status:
            status = True
        else:
            status = False
        Album.objects.create(title=title, banner=banner, status=status)
        return redirect(album)
    return render(request, "add_album.html")


# delete album list
def delete_album(request, target):
    if request.user.is_authenticated and request.user.is_superuser:
        data = Album.objects.get(id=target)
        Album.delete(data)
        return redirect(album)
    else:
        return render(request,"error.html")



# edit album
def edit_album(request, target):
    if request.user.is_authenticated and request.user.is_superuser:
        data = Album.objects.get(id=target)
        if request.method == "POST":
            datadict = request.POST
            title = datadict["title"]
            banner = False
            try:
                banner = request.FILES["banner"]
            except:
                pass
            status = datadict['PU']
            if status == "ON":
                status = True
            else:
                status = False
            data.title = title
            if banner:
                data.banner = banner
            data.status = status
            data.save()
            return redirect(album)
        d = {
            "album": data
        }
        return render(request, "edit_album.html", d)
    else:
        return render(request,"error.html")


# adding new song
def add_song(request):
    data = Album.objects.all()
    if request.method == "POST":
        datadict = request.POST
        album_id = datadict['album']
        alb = Album.objects.get(id=album_id)
        title = datadict['title']
        artist = datadict['artist']
        mp3 = request.FILES['mp3']
        status = datadict['status']
        if status == "on":
            status = True
        else:
            status = False
        Song.objects.create(album=alb, title=title, mp3=mp3, status=status, artist=artist)
        return redirect(album)
    d = {
        "alb": data
    }
    return render(request, 'new_song.html', d)


# login function
def Login(request):
    if request.user.is_authenticated:
        return redirect('album')
    error = False
    if request.method == "POST":
        datadict = request.POST
        user = datadict['un']
        password = datadict['ps']
        isuser = authenticate(username=user, password=password)
        if isuser:
            login(request, isuser)
            return redirect('album')
        error = True
    return render(request, "login.html", {'error': error})


# logout function
def Logout(request):
    logout(request)
    return redirect('login')


# add song in perticular are
def perticular(request,target):
    data = Album.objects.get(id=target)
    if request.method == "POST":
        dictdata = request.POST
        album_id = dictdata['opt']
        alb = Album.objects.get(id = album_id)
        title = dictdata['title']
        artist = dictdata['artist']
        mp3 = request.FILES['mp3']
        status = dictdata['PU']
        if status == 'on':
            status = True
        else:
            status = False
        print(alb,title,artist,mp3,status)
        Song.objects.create(album=alb,title= title,artist = artist,mp3 = mp3,status = status)
        return redirect(album_data, target)
    d = {
        'alb':data
    }
    return render(request,'perticular_song.html',d)


# delete Song
def song_del(request,target):
    print(request.GET)
    data = Song.objects.get(id = target)
    Song.delete(data)
    return redirect('album')


#register
def Register(request):
    if request.method == "POST":
        datadict = request.POST
        name = datadict['name']
        email = datadict['email']
        un = datadict['un']
        ps = datadict['ps']
        newuser = User.objects.create_user(username=un, email=email, password=ps)
        newuser.first_name = name
        newuser.save()
        return redirect('logout')
    return render(request, "register.html")
