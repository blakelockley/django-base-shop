from django.db import models
from .country import Country


class ShippingOption(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.country} (${self.price})"
