from typing import Optional
from django.db import models

from ..concrete.address import Address
from ..concrete.shipping_option import ShippingOption


class BaseCheckoutDetails(models.Model):
    class Meta:
        abstract = True

    customer_name = models.CharField(max_length=100)
    customer_company = models.CharField(max_length=100, blank=True)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=100)
    customer_coupon = models.CharField(max_length=100, blank=True)

    billing_name = models.CharField(max_length=100, blank=True)
    billing_company = models.CharField(max_length=100, blank=True)

    shipping_address = models.ForeignKey(
        Address, related_name="+", on_delete=models.PROTECT
    )

    billing_address_same_as_shipping = models.BooleanField(default=True)

    # Private field to be accessed via setter + getter
    _billing_address = models.ForeignKey(
        Address, null=True, related_name="+", on_delete=models.PROTECT
    )

    shipping_option = models.ForeignKey(
        ShippingOption, null=True, on_delete=models.PROTECT
    )

    @property
    def billing_address(self):
        """
        Return shipping or billing address based on billing_address_same_as_shipping flag.
        """

        if self.billing_address_same_as_shipping:
            return self.shipping_address

        return self._billing_address

    @billing_address.setter
    def billing_address(self, address):
        self.billing_address_same_as_shipping = False
        self._billing_address = address

        self.save()
