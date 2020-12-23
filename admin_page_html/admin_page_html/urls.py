from django.contrib import admin
from django.urls import path
from django.conf import  settings
from django.conf.urls.static import static
from Music.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('list/',album,name="album"),
    path('details/<int:target>/',album_data,name = "alb_data"),
    path("delete/<int:target>/",delete_album,name = "delete"),
    path('add/',add_album,name="add"),
    path('edit/<int:target>/',edit_album,name="edit"),
    path('song/',add_song,name = "song"),
    path('login/',Login,name="login"),
    path('logout/',Logout,name='logout'),
    path('perticular/<int:target>/',perticular,name="add_song"),
    path('del/<int:target>/',song_del,name='del'),
    path('register/',Register,name="register")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
