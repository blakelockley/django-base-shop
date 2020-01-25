from django.conf import settings
from django.db import models


class OrderItemManager(models.Manager):
    def create_from_cart_item(self, item, *, order: settings.SHOP_ORDER_MODEL):
        return self.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            unit_price_paid=item.product.price,
        )


class BaseOrderItem(models.Model):
    class Meta:
        abstract = True

    objects = OrderItemManager()

    order = models.ForeignKey(
        settings.SHOP_ORDER_MODEL, related_name="items", on_delete=models.PROTECT
    )
    product = models.ForeignKey(settings.SHOP_PRODUCT_MODEL, on_delete=models.PROTECT)

    unit_price_paid = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)

    @property
    def total_price(self):
        return self.unit_price_paid * self.quantity

    def clean(self, *args, **kwargs):
        super().clean()

        if self.quantity <= 0:
            raise ValidationError("Quantity of OrderItem must be greater than zero.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save()
