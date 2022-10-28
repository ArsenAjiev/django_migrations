from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=255)
    # artist = models.CharField(max_length=255)
    artist = models.ForeignKey('Artist', null=True, on_delete=models.CASCADE)


class Artist(models.Model):
    name = models.CharField(max_length=255)