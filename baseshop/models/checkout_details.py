from typing import Optional
from django.db import models

from .address import Address
from .shipping_option import ShippingOption


class CheckoutDetails(models.Model):
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=100)
    customer_coupon = models.CharField(max_length=100, blank=True)

    shipping_address = models.ForeignKey(
        Address, related_name="+", on_delete=models.PROTECT
    )
    billing_address = models.ForeignKey(
        Address, null=True, related_name="+", on_delete=models.PROTECT
    )

    billing_same_as_shipping = models.BooleanField(default=True)

    shipping_option = models.ForeignKey(
        ShippingOption, null=True, on_delete=models.PROTECT
    )

    @property
    def customer_name(self) -> str:
        return self.shipping_address.name

    @property
    def customer_company(self) -> Optional[str]:
        return self.shipping_address.company
