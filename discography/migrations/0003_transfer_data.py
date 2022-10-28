# Generated by Django 4.1.2 on 2022-10-28 07:37

from django.db import migrations


def link_artists(apps, schema_editor):
    Album = apps.get_model('discography', 'Album')
    Artist = apps.get_model('discography', 'Artist')
    for album in Album.objects.all():
        artist, created = Artist.objects.get_or_create(name=album.artist)
        album.artist_link = artist
        album.save()


class Migration(migrations.Migration):
    dependencies = [
        ('discography', '0002_artist_album_artist_link'),
    ]

    operations = [
        migrations.RunPython(link_artists),
    ]
