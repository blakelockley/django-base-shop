import pytest

from test_shop.models import ConcreteCheckoutDetails

pytestmark = pytest.mark.django_db


def test_checkout_details_billing_same_as_shipping(shipping_address):
    details = ConcreteCheckoutDetails()
    details.customer_name = "John Smith"
    details.customer_company = "ACME Corporation"
    details.shipping_address = shipping_address
    details.save()

    assert details.billing_address_same_as_shipping


def test_checkout_details_billing_differ_to_shipping(shipping_address, billing_address):
    details = ConcreteCheckoutDetails()
    details.customer_name = "John Smith"
    details.customer_company = "ACME Corporation"
    details.shipping_address = shipping_address

    details.billing_name = "Tim James"
    details.billing_company = "Offshore PTY LTD"
    details.billing_address = billing_address

    details.billing_address_same_as_shipping = False
    details.save()

    assert not details.billing_address_same_as_shipping
    assert details.billing_name == "Tim James"
    assert details.billing_company == "Offshore PTY LTD"
    assert details.billing_address == billing_address


def test_cehckout_details_has_billing(checkout_details):

    checkout_details.billing_address_same_as_shipping = True
    assert not checkout_details.has_billing

    checkout_details.billing_address_same_as_shipping = False
    assert checkout_details.has_billing


def test_cehckout_details_has_billing_setter(checkout_details):

    checkout_details.has_billing = True
    assert checkout_details.has_billing
    assert not checkout_details.billing_address_same_as_shipping
    
    checkout_details.has_billing = False
    assert not checkout_details.has_billing
    assert checkout_details.billing_address_same_as_shipping
