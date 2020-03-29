from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


class Holiday(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    date = models.DateField()

    def __str__(self):
        return "{} - {}".format(self.user, self.date)
