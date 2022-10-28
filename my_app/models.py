from django.db import models
import uuid
from randomslugfield import RandomSlugField


class MyModel(models.Model):
    char_id = models.CharField(max_length=32, primary_key=True, default='qwerty')
    slug_id = RandomSlugField(length=32, exclude_upper=True, unique=False)
    # slug_id = RandomSlugField(length=32, exclude_upper=True, primary_key=True)
    text = models.TextField(default='str')

