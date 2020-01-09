from functools import partial
from secrets import token_hex

from django.conf import settings
from django.db import models
from django.apps import apps

from .base_cart_item import BaseCartItem


class BaseCart(models.Model):
    class Meta:
        abstract = True
        indexes = (models.Index(fields=["cart_token"]),)

    # Used as a handle to retrieve the users cart from cookies or other
    cart_token = models.CharField(
        max_length=64, unique=True, editable=False, default=partial(token_hex, 32),
    )

    checkout_details = models.ForeignKey(
        settings.SHOP_CHECKOUT_DETAILS_MODEL,
        null=True,
        related_name="+",
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f"Cart ({self.cart_token})"

    @property
    def empty(self):
        return len(self) == 0

    @property
    def subtotal(self):
        total = 0
        for item in self.items.all():  # pylint: disable=no-member
            total += item.product.price * item.quantity
        return total

    def update_or_add_item(self, product, quantity=1):
        CartItem = apps.get_model(settings.SHOP_CART_ITEM_MODEL)
        item, _ = CartItem.objects.get_or_create(  # pylint: disable=no-member
            cart=self, product=product
        )
        item.quantity = quantity
        item.save()

    def remove_item(self, product):
        CartItem = apps.get_model(settings.SHOP_CART_ITEM_MODEL)
        CartItem.objects.filter(  # pylint: disable=no-member
            cart=self, product=product
        ).delete()
