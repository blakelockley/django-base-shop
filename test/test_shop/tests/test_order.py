from decimal import Decimal
import pytest
from django.core.exceptions import ValidationError
from test_shop.models import ConcreteCartItem, ConcreteOrder

pytestmark = pytest.mark.django_db


def test_order_token(product, cart):
    cart_item = ConcreteCartItem(cart=cart, product=product, quantity=1)
    cart_item.save()

    order = ConcreteOrder.objects.create_from_cart(cart)
    assert order.order_token is not None


def test_order_create(product, cart):
    cart_item = ConcreteCartItem(cart=cart, product=product, quantity=1)
    cart_item.save()

    original_shipping_price = cart.checkout_details.shipping_selection.price

    order = ConcreteOrder.objects.create_from_cart(cart)
    assert order.checkout_details == cart.checkout_details
    assert order.subtotal_paid == cart.subtotal
    assert order.shipping_paid == original_shipping_price
    assert order.total_paid == cart.subtotal + original_shipping_price


def test_order_shipping_price_changed(product, cart):
    cart_item = ConcreteCartItem(cart=cart, product=product, quantity=1)
    cart_item.save()

    original_shipping_price = cart.checkout_details.shipping_selection.price

    order = ConcreteOrder.objects.create_from_cart(cart)
    assert order.shipping_paid == original_shipping_price

    cart.checkout_details.shipping_selection.price = Decimal(37.5)
    assert order.shipping_paid != Decimal(37.5)
    assert order.shipping_paid == original_shipping_price


def test_order_len(product, cart):
    cart_item = ConcreteCartItem(cart=cart, product=product, quantity=1)
    cart_item.save()

    order = ConcreteOrder.objects.create_from_cart(cart)
    assert len(order) == 1
