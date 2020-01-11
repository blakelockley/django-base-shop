from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


class BaseCartItem(models.Model):
    class Meta:
        abstract = True

    cart = models.ForeignKey(
        settings.SHOP_CART_MODEL, related_name="items", on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(default=0)
    product = models.ForeignKey(settings.SHOP_PRODUCT_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return f"CartItem ({self.product.name} x {self.quantity})"

    @property
    def total_price(self):
        return self.product.price * self.quantity  # pylint: disable=no-member

    def clean(self, *args, **kwargs):
        super().clean()

        if self.quantity <= 0:
            raise ValidationError("Quantity of CartItem must be greater than zero.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save()
