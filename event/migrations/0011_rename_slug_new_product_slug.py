# Generated by Django 4.1.2 on 2022-10-28 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0010_remove_product_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='slug_new',
            new_name='slug',
        ),
    ]
