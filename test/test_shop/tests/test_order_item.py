import pytest
from django.core.exceptions import ValidationError
from test_shop.models import ConcreteCartItem, ConcreteOrderItem

pytestmark = pytest.mark.django_db


def test_order_item_create(product, cart, order):
    cart_item = ConcreteCartItem(cart=cart, product=product, quantity=1)
    cart_item.save()

    order_item = ConcreteOrderItem.objects.create_from_cart_item(cart_item, order=order)

    assert order_item.price_paid == product.price
    assert order_item.quantity == cart_item.quantity


def test_order_item_price_changed(product, cart, order):
    cart_item = ConcreteCartItem(cart=cart, product=product, quantity=1)
    cart_item.save()

    original_price = product.price

    order_item = ConcreteOrderItem.objects.create_from_cart_item(cart_item, order=order)

    assert order_item.price_paid == original_price

    # Changing the price of the product should not affect the order item
    product.price = 120.0
    product.save()

    assert order_item.price_paid != 120.0
    assert order_item.price_paid == original_price

