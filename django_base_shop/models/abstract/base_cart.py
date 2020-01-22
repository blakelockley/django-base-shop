from functools import partial
from secrets import token_hex

from django.conf import settings
from django.db import models
from django.apps import apps


class BaseCart(models.Model):
    class Meta:
        abstract = True
        indexes = (models.Index(fields=["cart_token"]),)

    # Used as a handle to retrieve the users cart from cookies or other
    cart_token = models.CharField(max_length=64, unique=True, editable=False,)

    checkout_details = models.ForeignKey(
        settings.SHOP_CHECKOUT_DETAILS_MODEL,
        null=True,
        related_name="+",
        on_delete=models.PROTECT,
    )

    def __str__(self):
        if not self.is_persisted:
            return f"Cart (Unpersisted)"

        return f"Cart ({self.cart_token[:8]})"

    def __len__(self):
        return self.items.count()  # pylint: disable=no-member

    @property
    def is_persisted(self):
        """
        Flag indicating if the cart has been stored in the db.
        """

        return bool(self.cart_token)

    @property
    def empty(self):
        return len(self) == 0

    @property
    def subtotal(self):
        total = 0
        for item in self.items.all():  # pylint: disable=no-member
            total += item.product.price * item.quantity
        return total

    def save(self, *args, **kwargs):

        if not self.cart_token:
            self.cart_token = token_hex(32)

        super().save(*args, **kwargs)

    def add_item(self, product, *, quantity=1):
        """
        Add item to cart. A single quantity will be added unless specified otherwise.
        """

        # Ensure we are using a persisted cart
        self.save()
        self.refresh_from_db()

        CartItem = apps.get_model(settings.SHOP_CART_ITEM_MODEL)

        item, created = CartItem.objects.get_or_create(
            cart=self, product=product, defaults={"quantity": quantity}
        )

        if not created:
            item.quantity += quantity
            item.save()

    def remove_item(self, product, *, quantity=None):
        """
        Remove item from cart. If quantity is None, the full quantity of the given item will be removed.
        """

        # Ensure we are using a persisted cart
        self.save()
        self.refresh_from_db()

        CartItem = apps.get_model(settings.SHOP_CART_ITEM_MODEL)
        item = CartItem.objects.get(cart=self, product=product)

        if quantity is None or quantity == item.quantity:
            CartItem.objects.filter(pk=item.pk).delete()

        else:
            item.quantity -= quantity
            item.save()

    def update_item(self, product, *, quantity):
        """
        Update item in cart to a specific quantity. A quantity of 0 will remove the item.
        """

        # Ensure we are using a persisted cart
        self.save()
        self.refresh_from_db()

        CartItem = apps.get_model(settings.SHOP_CART_ITEM_MODEL)

        item, created = CartItem.objects.get_or_create(
            cart=self, product=product, defaults={"quantity": quantity}
        )

        if not created:
            if quantity == 0:
                CartItem.objects.filter(pk=item.pk).delete()

            else:
                item.quantity = quantity
                item.save()
