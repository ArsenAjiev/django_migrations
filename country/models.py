from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'country- {self.name} - {self.code}'
