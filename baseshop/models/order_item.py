from django.db import models

from .product import Product
from .order import Order
from .cart_item import CartItem


class OrderItemManager(models.Manager):
    def create_from_cart_item(self, item, *, order: Order):
        return self.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price_paid=item.product.price,
        )


class OrderItem(models.Model):
    objects = OrderItemManager()

    order = models.ForeignKey(Order, related_name="items", on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    quantity = models.PositiveIntegerField(default=0)

    # Snapshot product price info
    price_paid = models.DecimalField(max_digits=7, decimal_places=2)

    @property
    def combined_price(self):
        return self.price_paid * self.quantity
