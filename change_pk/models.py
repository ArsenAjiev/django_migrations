import uuid
from django.db import models
from django.utils.crypto import get_random_string

# print(get_random_string(32))


class Product(models.Model):
    # uuid_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    uuid_id = models.UUIDField(default=uuid.uuid4)
    details = models.TextField(default='some text')
    slug = models.SlugField(blank=True, max_length=255, primary_key=True)
    # 2- add slug new
    # slug_new = models.SlugField(blank=True, max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_str = get_random_string(7)
            self.slug = slug_str
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'id = {self.uuid_id}, ||| slug = {self.slug} ||| detail: {self.slug}'

