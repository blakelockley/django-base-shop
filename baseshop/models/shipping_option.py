from django.db import models

from .country import Country


class ShippingOption(models.Model):
    NONE = "N"
    SMALL = "S"
    MEDIUM = "M"
    LARGE = "L"

    SIZE_CHOICES = [
        (NONE, "None"),
        (SMALL, "Small"),
        (MEDIUM, "Medium"),
        (LARGE, "Large"),
    ]

    REGULAR = "R"
    EXPRESS = "E"

    TYPE_CHOICES = [(REGULAR, "Regular"), (EXPRESS, "Express")]

    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    shipping_type = models.CharField(max_length=1, choices=TYPE_CHOICES)

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.country
