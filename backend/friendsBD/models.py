from django.conf import settings
from django.db import models


class M1(models.Model):
    "Generated Model"
    timeline = models.TimeField(auto_now=True,)
    field = models.TimeField(auto_now_add=True, null=True, blank=True,)
    m2 = models.BigIntegerField(null=True, blank=True,)


# Create your models here.
