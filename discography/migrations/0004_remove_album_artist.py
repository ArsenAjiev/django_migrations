# Generated by Django 4.1.2 on 2022-10-28 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discography', '0003_transfer_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='artist',
        ),
    ]
