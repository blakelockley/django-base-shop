from functools import partial
from secrets import token_hex

from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from django.db import models

from .cart_item import CartItem
from .checkout_details import CheckoutDetails


class Cart(models.Model):
    class Meta:
        indexes = (models.Index(fields=["cart_token"]),)

    cart_token = models.CharField(
        max_length=32, unique=True, editable=False, default=partial(token_hex, 16)
    )
    checkout_details = models.ForeignKey(
        CheckoutDetails, null=True, related_name="+", on_delete=models.PROTECT
    )

    def __str__(self):
        return f"Cart ({self.session.session_key})"

    @property
    def empty(self):
        return len(self) == 0

    @property
    def subtotal(self):
        total = 0
        for item in self.items.all():
            total += item.product.price * item.quantity
        return total

    def update_or_add_item(self, product, quantity=1):
        item, _ = CartItem.objects.get_or_create(cart=self, product=product)
        item.quantity = quantity
        item.save()

    def remove_item(self, product):
        CartItem.objects.filter(cart=self, product=product).delete()
