
from django.contrib import admin
from django.urls import path
from album.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', check),
    path('list/', ablum_list, name="list"),
    path('details/<int:target>/', song_list, name="details")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
