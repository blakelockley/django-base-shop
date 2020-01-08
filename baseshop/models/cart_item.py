from django.core.exceptions import ValidationError
from django.db import models

from .product import Product


class CartItem(models.Model):
    cart = models.ForeignKey("Cart", related_name="items", on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def __str__(self):
        return f"CartItem ({self.product.name} x {self.quantity})"

    @property
    def combined_price(self):
        return self.product.price * self.quantity

