from django.db import models
from django.contrib.auth import user


class Room(models):
    floor = models.SmallIntegerField(null=False, blank=False)
    reservation_date = models.DateTimeField()
    client = models.ForeignKey(user, on_delete=models.CASCADE)
