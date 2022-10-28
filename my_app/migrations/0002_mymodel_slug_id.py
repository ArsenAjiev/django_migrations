# Generated by Django 4.1.2 on 2022-10-27 14:12

from django.db import migrations
import randomslugfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='slug_id',
            field=randomslugfield.fields.RandomSlugField(blank=True, editable=False, exclude_upper=True, length=32, max_length=32, unique=True),
        ),
    ]