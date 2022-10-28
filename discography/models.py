from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    # add new attribute
    artist_link = models.ForeignKey('Artist', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f' name: {self.name} - artist: {self.artist}'


# add new related model
class Artist(models.Model):
    name = models.CharField(max_length=255)
