from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=50, default=None)
    artist = models.CharField(max_length=50, default=None)
    album = models.CharField(max_length=50, default=None)
    release_date = models.DateField(null=True, blank=False)
    like = models.IntegerField(default=0, null=True)
