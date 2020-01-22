from django.db import models

from .country import Country


class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20)

    country = models.ForeignKey(Country, on_delete=models.PROTECT)
