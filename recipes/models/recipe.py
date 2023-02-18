from django.db import models

class Recipe(models.Model):
    name = models.CharField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)