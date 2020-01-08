from django.contrib.sessions.models import Session
from django.test import TestCase
from django.db import transaction

from shop.models import (
    Address,
    Cart,
    CheckoutDetails,
    Country,
    Order,
    Product,
    ShippingOption,
)


class OrderTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.australia, _ = Country.objects.get_or_create(name="Australia")

        cls.address = Address.objects.create(
            name="John Smith",
            company="Business PTY LTD",
            line="42 Bridge Street",
            city="Sydney",
            state="NSW",
            postcode="2000",
            country=cls.australia,
        )

        cls.checkout_details = CheckoutDetails.objects.create(
            customer_email="john.smith@mail.com",
            customer_phone="0401 123 456",
            shipping_address=cls.address,
        )

        cls.product = Product.objects.create(
            name="Product A", part_number="PRODUCT-A", price=100.00
        )

        cls.shipping_option = ShippingOption.objects.create(
            country=cls.australia, price=10.00
        )

    def test_order_cant_create_without_shipping(self):

        session = Session.objects.get(session_key=self.client.session.session_key)
        cart, _ = Cart.objects.get_or_create(session=session)

        cart.update_or_add_item(self.product)
        assert cart.items.count() == 1

        cart.checkout_details = self.checkout_details
        cart.save()

        assert cart.checkout_details is not None

        with transaction.atomic():
            self.assertRaises(ValueError, lambda: Order.objects.create_from_cart(cart))

    def test_order_create(self):

        session = Session.objects.get(session_key=self.client.session.session_key)
        cart, _ = Cart.objects.get_or_create(session=session)

        cart.update_or_add_item(self.product)
        assert cart.items.count() == 1

        cart.checkout_details = self.checkout_details
        cart.save()

        assert cart.checkout_details is not None

        cart.checkout_details.shipping_option = self.shipping_option
        cart.save()

        assert cart.checkout_details.shipping_option is not None

        order = Order.objects.create_from_cart(cart)
        order.checkout_details == self.checkout_details

        order.items.count() == 1
