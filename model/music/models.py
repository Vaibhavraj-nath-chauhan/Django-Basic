from django.db import models

class songs(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date = models.DateTimeField()
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.title
