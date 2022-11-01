import uuid
from django.db import models
from django.utils.crypto import get_random_string


#  step_1
# class Product(models.Model):
#     uuid_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#     details = models.TextField(default='some text')


#  step_2
# class Product(models.Model):
#     uuid_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#     details = models.TextField(default='some text')
#     slug = models.SlugField(blank=True)
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             slug_str = get_random_string(7)
#             self.slug = slug_str
#         return super().save(*args, **kwargs)
#
#     def __str__(self):
#         return f'id = {self.uuid_id}, ||| slug = {self.slug}'


#  step_3
class Product(models.Model):
    uuid_id = models.UUIDField(default=uuid.uuid4)
    details = models.TextField(default='some text')
    slug = models.SlugField(blank=True, primary_key=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_str = get_random_string(7)
            self.slug = slug_str
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'id = {self.uuid_id}, ||| slug = {self.slug}'



