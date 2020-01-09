from django.db import models

# TODO: ...
# from images.models import Image


class BaseProduct(models.Model):
    class Meta:
        abstract = True
        ordering = ["-order_priority"]

    # Identifiers
    handle = models.CharField(
        max_length=200,
        unique=True,
        help_text="Unique idenitfier used select specific product.",
    )

    # Descriptive info
    name = models.CharField(max_length=200)
    description = models.TextField()

    # TODO: Implement with FK model;
    # images = models.ManyToManyField(Image)

    # Pricing
    price = models.DecimalField(max_digits=7, decimal_places=2)

    # TODO: Abstract
    # shipping_size = models.CharField(
    #     max_length=1,
    #     choices=ShippingOption.SIZE_CHOICES,
    #     default=ShippingOption.MEDIUM,
    # )

    # Availablity
    available = models.BooleanField(default=True)
    back_in_stock = models.DateField(null=True, blank=True)

    # Admin only
    order_priority = models.PositiveSmallIntegerField(
        default=1000, help_text="Hint on how the product should be displayed in lists."
    )

    def __str__(self):
        return f"{self.name} ({self.handle})"

    @property
    def first_image(self):
        pass
        # return self.images.all().first()
