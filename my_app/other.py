from django.db import models
import uuid
from randomslugfield import RandomSlugField
from django.utils.text import slugify
import datetime


def time_to_sec(var):
    time_1 = str(var)
    date_time = datetime.datetime.strptime(time_1, "%H:%M:%S")
    a_timedelta = date_time - datetime.datetime(1900, 1, 1)
    seconds = a_timedelta.total_seconds()
    return int(seconds)


# class MyModel(models.Model):
#     field_name = models.PositiveIntegerField()
#
#     def __str__(self):
#         # return f'{self.field_name} -second:  {time_to_sec(self.field_name)} '
#         return f'{self.field_name} '


class MyModel(models.Model):
    field_name_old = models.TextField()

    def __str__(self):
        # return f'{self.field_name} -second:  {time_to_sec(self.field_name)} '
        return f'{self.field_name_old}'




# class Country(models.Model):
#     name = models.CharField(max_length=255, null=True, blank=True)
#     code = models.CharField(max_length=255, null=True, blank=True)
#
#     def __str__(self):
#         return f'country- {self.name} - {self.code}'
#
#
# class UUIDModel(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     text = models.TextField(default='str')
#
#     def __str__(self):
#         return f'id - {self.id}'
#
#
# class SlugModel(models.Model):
#     slug_id = RandomSlugField(length=32, exclude_upper=True, primary_key=True)
#     title = models.TextField(default='asdfgh')
#
#     def __str__(self):
#         return f' slug_id: {self.slug_id}'


# class Article(models.Model):
#     slug = models.SlugField(primary_key=True)
#     headline = models.CharField(max_length=100)
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.headline)
#         # self.slug = new_slug()
#         super(Article, self).save(*args, **kwargs)