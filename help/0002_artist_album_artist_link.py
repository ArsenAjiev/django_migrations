# Generated by Django 4.1.2 on 2022-10-27 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artist_link',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.artist'),
        ),
    ]
