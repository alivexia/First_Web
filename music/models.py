from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=512)
    album_title = models.CharField(max_length=512)
    genre = models.CharField(max_length=96)
    album_logo = models.CharField(max_length=1024)
    album_introduction = models.TextField(default='')

    def __str__(self):
        return self.album_title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=16)
    song_title = models.CharField(max_length=512)
    Favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
