from django.db import models

from .country import Country


class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20)

    country = models.ForeignKey(Country, on_delete=models.PROTECT)

    @property
    def formatted(self) -> str:
        return f"{self.street}\n{self.city} {self.state} {self.postcode}\n{self.country.name}"

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.country.name} ({self.postcode})"
