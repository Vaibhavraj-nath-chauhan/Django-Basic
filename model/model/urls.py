
from django.contrib import admin
from django.urls import path
from music.views import data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('details/',data),
]
