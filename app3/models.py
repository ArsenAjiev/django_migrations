import uuid

from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.TextField()
    # slug = models.SlugField(primary_key=True)
    slug_no = models.SlugField(primary_key=True)
    # uuid_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    uuid_id2 = models.UUIDField(default=uuid.uuid4)
