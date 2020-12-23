
from django.contrib import admin
from django.urls import path
from Music.views import html,perticular
urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/',html),
    path("details/<int:id>/",perticular),
]
