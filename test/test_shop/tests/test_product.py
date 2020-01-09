import pytest

pytestmark = pytest.mark.django_db


def test_product_id(product):
    assert product.id is not None  # pylint: disable=no-member


def test_product_str(product):
    assert str(product) == "Anvil (ANV-001)"


def test_product_available(product):
    assert product.available
