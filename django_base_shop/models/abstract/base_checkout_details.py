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

    billing_address_same_as_shipping = models.BooleanField(default=True)

    # Private billing details fields to be accessed via setter + getter
    #   These fields will default to the customer/shipping information depending on
    #   the state of the 'billing_address_same_as_shipping' flag.
    _billing_name = models.CharField(max_length=100, blank=True)
    _billing_company = models.CharField(max_length=100, blank=True)
    _billing_address = models.ForeignKey(
        Address, null=True, related_name="+", on_delete=models.PROTECT
    )

    @property
    def billing_name(self):
        if self.billing_address_same_as_shipping:
            return self.customer_name
        return self._billing_name

    @billing_name.setter
    def billing_name(self, name):
        self._billing_name = name

    @property
    def billing_company(self):
        if self.billing_address_same_as_shipping:
            return self.customer_company
        return self._billing_company

    @billing_company.setter
    def billing_company(self, company):
        self._billing_company = company

    @property
    def billing_address(self):
        if self.billing_address_same_as_shipping:
            return self.shipping_address
        return self._billing_address

    @billing_address.setter
    def billing_address(self, address):
        self._billing_address = address
