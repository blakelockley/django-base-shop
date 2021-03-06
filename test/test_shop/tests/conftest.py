from decimal import Decimal
import pytest
from django_base_shop.models import Country, Address, ShippingOption, ShippingTag
from test_shop.models import (
    ConcreteProduct,
    ConcreteCart,
    ConcreteOrder,
    ConcreteCheckoutDetails,
)


@pytest.fixture
def australia():
    return Country.objects.create(name="Australia (Fixture)")


@pytest.fixture
def shipping_tag():
    return ShippingTag.objects.create(name="Medium", category="Size", order=1)


@pytest.fixture
def basic_shipping_option(australia, shipping_tag):
    return ShippingOption.objects.create(
        name="Regular",
        price=Decimal(10.0),
        country=australia,
        shipping_tag=shipping_tag,
    )


@pytest.fixture
def shipping_address(australia):
    address = Address()
    address.street = "123 Home Street"
    address.city = "Sydney"
    address.state = "NSW"
    address.postcode = "2000"
    address.country = australia
    address.save()

    return address


@pytest.fixture
def billing_address(australia):
    address = Address()
    address.street = "456 Other Street"
    address.city = "Melbourne"
    address.state = "VIC"
    address.postcode = "3000"
    address.country = australia
    address.save()

    return address


@pytest.fixture
def product(shipping_tag):
    anvil_product = ConcreteProduct()
    anvil_product.handle = "ANV-001"
    anvil_product.name = "Anvil"
    anvil_product.description = "Great product!"
    anvil_product.price = Decimal(100.0)
    anvil_product.shipping_tag = shipping_tag
    anvil_product.save()

    return anvil_product


@pytest.fixture
def extra_product(shipping_tag):
    tnt_product = ConcreteProduct()
    tnt_product.handle = "TNT-001"
    tnt_product.name = "TNT"
    tnt_product.description = "KABOOM!"
    tnt_product.price = Decimal(50.0)
    tnt_product.shipping_tag = shipping_tag
    tnt_product.save()

    return tnt_product


@pytest.fixture
def checkout_details(shipping_address, basic_shipping_option):
    return ConcreteCheckoutDetails.objects.create(
        customer_name="John Smith",
        shipping_address=shipping_address,
        shipping_selection=basic_shipping_option,
    )


@pytest.fixture
def cart(checkout_details):
    return ConcreteCart.objects.create(checkout_details=checkout_details)


@pytest.fixture
def order(cart):
    return ConcreteOrder.objects.create_from_cart(cart)

