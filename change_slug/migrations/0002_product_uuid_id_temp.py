# Generated by Django 4.1.2 on 2022-11-01 11:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('change_slug', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='uuid_id_temp',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
