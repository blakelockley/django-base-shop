from django.db import models
from .country import Country


class ShippingTag(models.Model):
    """
    Shipping information about a product or multiple products used to determine the shipping options avaliable for the final order.
    """

    class Meta:
        unique_together = ("category", "order")
        ordering = ["category", "order"]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    order = models.PositiveSmallIntegerField(
        default=0, help_text="Order of tag for the given category."
    )

    def __str__(self):
        return f"{self.category}: {self.name}"
