from django.db import models

# Create your models here.


class Song(models.Model):
    song_id=models.AutoField(primary_key=True)
    song_name=models.CharField(max_length=20)
    song_genre=models.CharField(max_length=15)
