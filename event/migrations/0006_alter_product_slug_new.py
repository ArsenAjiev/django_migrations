# Generated by Django 4.1.2 on 2022-10-28 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_transfer_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug_new',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
