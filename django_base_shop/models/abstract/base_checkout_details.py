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

    shipping_selection = models.ForeignKey(
        ShippingOption, null=True, on_delete=models.PROTECT
    )

    shipping_address = models.ForeignKey(
        Address, related_name="+", on_delete=models.PROTECT
    )

    billing_address_same_as_shipping = models.BooleanField(
        default=True, verbose_name="Billing same as shipping"
    )

    billing_name = models.CharField(max_length=100, blank=True)
    billing_company = models.CharField(max_length=100, blank=True)
    billing_address = models.ForeignKey(
        Address, null=True, blank=True, related_name="+", on_delete=models.PROTECT
    )

    def __str__(self):
        if self.customer_name:
            return f"CheckoutDetails ({self.customer_name})"

        return super().__str__()

    @property
    def has_billing(self):
        """
        CheckoutDetails contains unique billing information.
        """

        return not self.billing_address_same_as_shipping

    @has_billing.setter
    def has_billing(self, flag):
        """
        Specify that the CheckoutDetails contains unique billing information.
        Note, the model instance is still required to be saved after setting this property.
        """

        self.billing_address_same_as_shipping = not flag
