from django.db import models


class HblTeam(models.Model):
    name = models.CharField()
    abbr = models.CharField(max_length=3)
    owner = models.ForeignKey('User', related_name='hbl_team', unique=True, on_delete=models.SET_NULL)
