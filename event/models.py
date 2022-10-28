import uuid
from django.db import models
from django.utils.crypto import get_random_string

# print(get_random_string(32))


class Product(models.Model):
    uuid_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    details = models.TextField(default='some text')
    slug = models.SlugField(blank=True, null=True)
    slug_new = models.SlugField(blank=True, null=True, max_length=32, unique=True)

    def save(self, *args, **kwargs): # new
        if not self.slug:
            slug_str = get_random_string(32)
            self.slug = slug_str
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'id = {self.uuid_id}, ||| slug_new = {self.slug_new} ||| slug: {self.slug}'




