from django.db import models
from .country import Country
from .shipping_tag import ShippingTag


class ShippingOption(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    # Look up criteria
    country = models.ForeignKey(Country, null=True, on_delete=models.CASCADE)
    shipping_tag = models.ForeignKey(ShippingTag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} (${self.price})"
