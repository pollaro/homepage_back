from django.db import models

class Measurement(models.Model):

    class Types(models.TextChoices):
        VOLUME_LIQUID = 'VL'
        VOLUME_SOLID = 'VS'
        MASS = 'MA'

    name = models.CharField()
    abbreviation = models.CharField()
    type = models.CharField(choices=Types.choices)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)