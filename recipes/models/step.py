from django.db import models

class Step(models.Model):
    number = models.IntegerField()
    direction = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)