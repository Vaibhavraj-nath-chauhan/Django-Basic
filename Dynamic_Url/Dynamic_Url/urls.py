
from django.contrib import admin
from django.urls import path
from dy_url.views import studens,dynamic

urlpatterns = [
    path('admin/', admin.site.urls),
    path("list/",studens),
    path("details/<int:my_details>/",dynamic),    #creating dynamic url which read url value
]
