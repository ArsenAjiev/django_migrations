# Generated by Django 4.1.2 on 2022-11-01 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('change_pk', '0006_remove_product_uuid_id_alter_product_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='uuid_id_new',
            new_name='uuid_id',
        ),
    ]