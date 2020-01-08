from django.test import TestCase
from django.contrib.sessions.models import Session

from shop.models import Country
from shop.models import Address
from shop.models import Cart
from shop.models import Product
from shop.models import CheckoutDetails


class CartTestCase(TestCase):
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

    def test_cart_create(self):
        session = Session.objects.get(session_key=self.client.session.session_key)
        cart, _ = Cart.objects.get_or_create(session=session)

        assert cart.session is not None

    def test_cart_add_product(self):

        session = Session.objects.get(session_key=self.client.session.session_key)
        cart, _ = Cart.objects.get_or_create(session=session)

        cart.update_or_add_item(self.product)
        assert cart.items.count() == 1

    def test_cart_remove_product(self):

        session = Session.objects.get(session_key=self.client.session.session_key)
        cart, _ = Cart.objects.get_or_create(session=session)

        cart.update_or_add_item(self.product)
        assert cart.items.count() == 1

        cart.remove_item(self.product)
        assert cart.items.count() == 0

    def test_cart_checkout_details(self):
        session = Session.objects.get(session_key=self.client.session.session_key)
        cart, _ = Cart.objects.get_or_create(session=session)

        assert self.checkout_details.customer_name == "John Smith"
        assert self.checkout_details.customer_company == "Business PTY LTD"

    def test_cart_checkout_details_fk(self):
        session = Session.objects.get(session_key=self.client.session.session_key)
        cart, _ = Cart.objects.get_or_create(session=session)

        cart.checkout_details = self.checkout_details
        cart.save()

        assert cart.checkout_details is not None

