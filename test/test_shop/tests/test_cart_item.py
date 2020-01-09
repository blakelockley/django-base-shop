import pytest
from django.core.exceptions import ValidationError
from test_shop.models import ConcreteCartItem

pytestmark = pytest.mark.django_db


def test_cart_item_total_price(product, cart):
    cart_item = ConcreteCartItem(cart=cart, product=product, quantity=1)
    cart_item.save()

    assert cart_item.total_price == product.price

    cart_item.quantity = 5
    cart_item.save()

    assert cart_item.total_price == product.price * 5


def test_cart_item_zero_quantity(product, cart):
    cart_item = ConcreteCartItem(cart=cart, product=product, quantity=0)

    with pytest.raises(ValidationError):
        cart_item.save()
