from django.db import models

# Create your models here.
class album(models.Model):
    title = models.CharField(max_length=50)
    banner = models.CharField(max_length=400)
    singer = models.CharField(max_length=40)
    date = models.DateField()
    status = models.BooleanField(default="False")

    def __str__(self):
        return self.title
