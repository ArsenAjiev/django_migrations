# Generated by Django 4.1.2 on 2022-11-01 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('change_pk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug_new',
            field=models.SlugField(blank=True, max_length=255),
        ),
    ]