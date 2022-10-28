This is likely a case where you want to do a multi-stage migration. My recommendation for this would look something like the following.

First off, let's assume this is your initial model, inside an application called discography:
```shell
from django.db import models

class Album(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
```

Now, you realize that you want to use a ForeignKey for the artist instead. Well, as mentioned, this is not just a simple process for this. It has to be done in several steps.

Step 1, add a new field for the ForeignKey, making sure to mark it as null:
```shell
from django.db import models

class Album(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    artist_link = models.ForeignKey('Artist', null=True)

class Artist(models.Model):
    name = models.CharField(max_length=255)
...and create a migration for this change.

./manage.py makemigrations discography
```

Step 2, populate your new field. In order to do this, you have to create an empty migration.
```shell
./manage.py makemigrations --empty --name transfer_artists discography
```

Once you have this empty migration, you want to add a single RunPython operation to it in order to link your records. In this case, it could look something like this:

```shell
def link_artists(apps, schema_editor):
    Album = apps.get_model('discography', 'Album')
    Artist = apps.get_model('discography', 'Artist')
    for album in Album.objects.all():
        artist, created = Artist.objects.get_or_create(name=album.artist)
        album.artist_link = artist
        album.save()
```

Now that your data is transferred to the new field, you could actually be done and leave everything as is, using the new field for everything. Or, if you want to do a bit of cleanup, you want to create two more migrations.
```text
For your first migration, you will want to delete your original field, artist. 
```

```text
For your second migration, rename the new field artist_link to artist.
```


This is done in multiple steps to ensure that Django recognizes the operations properly. You could create a migration manually to handle this, but I will leave that to you to figure out.