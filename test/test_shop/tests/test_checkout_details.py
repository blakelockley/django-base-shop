import pytest

from django_base_shop.models import Country, Address
from test_shop.models import ConcreteCheckoutDetails

pytestmark = pytest.mark.django_db


@pytest.fixture
def australia():
    return Country.objects.create(name="Australia (Fixture)")


@pytest.fixture
def shipping_address(australia):
    address = Address()
    address.line = "123 Home Street"
    address.city = "Sydney"
    address.state = "NSW"
    address.postcode = "2000"
    address.country = australia
    address.save()

    return address


@pytest.fixture
def billing_address(australia):
    address = Address()
    address.line = "456 Other Street"
    address.city = "Melbourne"
    address.state = "VIC"
    address.postcode = "3000"
    address.country = australia
    address.save()

    return address


def test_checkout_details_billing_same_as_shipping(shipping_address):

    details = ConcreteCheckoutDetails()
    details.shipping_address = shipping_address
    details.save()

    assert details.billing_address_same_as_shipping
    assert details.billing_address == shipping_address


def test_checkout_details_billing_different_to_shipping(
    shipping_address, billing_address
):

    details = ConcreteCheckoutDetails()
    details.shipping_address = shipping_address
    details.billing_address = billing_address
    details.save()

    assert not details.billing_address_same_as_shipping
    assert details.billing_address == billing_address
