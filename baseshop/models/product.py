from ckeditor.fields import RichTextField
from django.db import models

from images.models import Image

from .shipping_option import ShippingOption


class Product(models.Model):
    class Meta:
        ordering = ["-order_priority"]

    # Descriptive info
    name = models.CharField(max_length=200)
    description = RichTextField()

    # Identifiers
    part_number = models.CharField(max_length=200, unique=True)
    alt_part_numbers = models.CharField(max_length=200, blank=True)

    # Images
    images = models.ManyToManyField(Image)

    # Pricing
    price = models.DecimalField(max_digits=7, decimal_places=2)
    shipping_size = models.CharField(
        max_length=1, choices=ShippingOption.SIZE_CHOICES, default=ShippingOption.MEDIUM
    )

    # Availability
    availabile = models.BooleanField(default=True)
    back_in_stock = models.DateField(null=True, blank=True)

    # Admin only
    order_priority = models.PositiveSmallIntegerField(default=1000)

    def __str__(self):
        return f"{self.name} ({self.part_number})"

    @property
    def first_image(self):
        return self.images.all().first()
