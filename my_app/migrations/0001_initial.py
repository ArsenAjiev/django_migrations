# Generated by Django 4.1.2 on 2022-10-27 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('char_id', models.CharField(default='qwerty', max_length=32, primary_key=True, serialize=False)),
                ('text', models.TextField(default='str')),
            ],
        ),
    ]
