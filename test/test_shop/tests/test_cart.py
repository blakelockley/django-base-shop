import pytest
from django.core.exceptions import ValidationError
from django.test import Client

from test_shop.models import ConcreteCart, ConcreteCartItem

pytestmark = pytest.mark.django_db


def test_cart_token(cart):
    cart_token = cart.cart_token
    assert bool(cart_token)

    retreived_cart = ConcreteCart.objects.get(cart_token=cart_token)
    assert retreived_cart == cart


def test_cart_count(cart, product, extra_product):
    assert len(cart) == 0
    assert cart.empty

    cart_item = ConcreteCartItem(cart=cart, product=product, quantity=1)
    cart_item.save()

    assert len(cart) == 1
    assert not cart.empty

    cart_item = ConcreteCartItem(cart=cart, product=extra_product, quantity=1)
    cart_item.save()

    assert len(cart) == 2
    assert not cart.empty


def test_cart_subtotal(cart, product, extra_product):

    # Add products
    cart_item = ConcreteCartItem(cart=cart, product=product, quantity=2)
    cart_item.save()

    cart_item = ConcreteCartItem(cart=cart, product=extra_product, quantity=1)
    cart_item.save()

    assert cart.subtotal == 250.0  # Total 100 * 2 (product) + 50 (extra_product)


def test_cart_total(cart, product, checkout_details):

    # Add products
    cart_item = ConcreteCartItem(cart=cart, product=product, quantity=1)
    cart_item.save()

    cart.checkout_details = checkout_details
    cart.save()

    assert cart.subtotal == 100.0
    assert checkout_details.shipping_selection.price == 10.0

    assert cart.total == 110.0


def test_cart_add_item(cart, product, extra_product):
    cart.add_item(product)
    assert len(cart) == 1

    cart.add_item(extra_product)
    assert len(cart) == 2


def test_cart_add_item_multiple(cart, product):
    cart.add_item(product, quantity=2)

    assert len(cart) == 1
    assert cart.items.first().quantity == 2


def test_cart_add_item_zero(cart, product):
    with pytest.raises(ValidationError):
        cart.add_item(product, quantity=0)


def test_cart_remove_item(cart, product):
    assert len(cart) == 0

    cart.add_item(product)
    assert len(cart) == 1

    cart.remove_item(product)
    assert len(cart) == 0


def test_cart_remove_item_multiple(cart, product):
    cart.add_item(product, quantity=10)
    assert cart.items.first().quantity == 10

    cart.remove_item(product, quantity=3)
    assert cart.items.first().quantity == 7

    cart.remove_item(product, quantity=7)
    assert len(cart) == 0


def test_cart_update_item(cart, product):
    cart.add_item(product, quantity=10)
    assert cart.items.first().quantity == 10

    cart.update_item(product, quantity=7)
    assert cart.items.first().quantity == 7

    cart.update_item(product, quantity=0)
    assert len(cart) == 0


def test_cart_clear(cart, product):
    cart.add_item(product, quantity=10)

    assert cart.id is not None

    cart.clear()
    assert cart.id is None


def test_cart_middleware():
    client = Client()

    # Cart on request should be set to None
    response = client.get("/check_cart")
    assert response.content == b"None"

    # Add item to the cart
    response = client.get("/add_cart_item/1")
    assert response.status_code == 200

    # Get cart from db
    cart = ConcreteCart.objects.first()

    # Cart on request should now match only cart in db
    response = client.get("/check_cart")
    assert response.content == bytes(cart.cart_token, encoding="utf-8")
