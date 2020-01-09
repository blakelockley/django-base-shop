import pytest
from test_shop.models import ConcreteProduct, ConcreteCart


@pytest.fixture
def product():
    anvil_product = ConcreteProduct()
    anvil_product.handle = "ANV-001"
    anvil_product.name = "Anvil"
    anvil_product.description = "Great product!"
    anvil_product.price = 100.0
    anvil_product.save()

    return anvil_product


@pytest.fixture
def extra_product():
    tnt_product = ConcreteProduct()
    tnt_product.handle = "TNT-001"
    tnt_product.name = "TNT"
    tnt_product.description = "KABOOM!"
    tnt_product.price = 50.0
    tnt_product.save()

    return tnt_product


@pytest.fixture
def cart():
    return ConcreteCart.objects.create()
