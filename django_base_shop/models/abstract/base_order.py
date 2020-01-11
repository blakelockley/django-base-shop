from decimal import Decimal
from functools import partial
from secrets import token_hex

from django.db import models
from django.conf import settings
from django.apps import apps

from ..abstract.base_cart import BaseCart


class OrderManager(models.Manager):
    def create_from_cart(self, cart: BaseCart):

        if cart.checkout_details.shipping_selection is None:
            raise ValueError(
                "Cart must contain a shipping option when creating an Order."
            )

        # TODO: Atomic transaction and destory cart
        order = self.create(
            checkout_details=cart.checkout_details,
            shipping_paid=cart.checkout_details.shipping_selection.price,
            subtotal_paid=cart.subtotal,
        )

        OrderItem = apps.get_model(settings.SHOP_ORDER_ITEM_MODEL)

        for item in cart.items.all():
            OrderItem.objects.create_from_cart_item(item, order=order)

        return order


class BaseOrder(models.Model):
    class Meta:
        abstract = True
        indexes = (models.Index(fields=["order_token"]),)

    objects = OrderManager()

    # Meta info
    date_placed = models.DateTimeField(auto_now_add=True)
    order_token = models.CharField(
        max_length=32, unique=True, editable=False, default=partial(token_hex, 16)
    )

    # TODO: Make the values of the related object inmutable once set
    checkout_details = models.ForeignKey(
        settings.SHOP_CHECKOUT_DETAILS_MODEL, related_name="+", on_delete=models.PROTECT
    )

    # Snapshot price information
    #   This is done incase price of FK field is updated.
    subtotal_paid = models.DecimalField(max_digits=7, decimal_places=2)
    shipping_paid = models.DecimalField(max_digits=7, decimal_places=2)

    def __len__(self):
        return self.items.count()

    def __str__(self):
        return f"Order ({self.checkout_details.customer_name})"

    @property
    def total_paid(self):
        return self.subtotal_paid + self.shipping_paid
