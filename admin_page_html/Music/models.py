from django.db import models
from datetime import date
# Create your models here.

# creating our ablum
class Album(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(default=date.today)
    banner = models.FileField(max_length=400,upload_to="Album")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# now we will add our data here
class Song(models.Model):
    album = models.ForeignKey(Album,models.CASCADE)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=40)
    mp3 = models.FileField(max_length=400,upload_to="songs")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title