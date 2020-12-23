from django.db import models

# Create your models here.

class AlbumData(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    banner = models.FileField(upload_to="Banner")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Songs_list(models.Model):
    album = models.ForeignKey(AlbumData,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length= 30)
    artist = models.CharField(max_length= 30,default="Unknown")
    audio = models.FileField(upload_to="audio" , null=True,max_length=200)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
