import datetime

from django.db import models


class HblUser(models.Model):
    email = models.EmailField()
    token = models.CharField(null=True)
    refresh_token = models.CharField(null=True)
    expiration_time = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if self.token:
            self.expiration_time = datetime.datetime.now() + datetime.timedelta(
                seconds=3600
            )
        super().save()
