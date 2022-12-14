# Generated by Django 4.1.2 on 2022-10-28 09:52

from django.db import migrations

def link_slug(apps, schema_editor):
    Product = apps.get_model('event', 'Product')
    for prod in Product.objects.all():
        slug_n, created = Product.objects.get_or_create(uuid_id=prod.uuid_id)
        prod.slug_new = str(slug_n)
        prod.save()

class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_alter_product_slug_new'),
    ]

    operations = [
        migrations.RunPython(link_slug),
    ]
