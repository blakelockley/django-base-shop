import pytest

from django_base_shop.models import ShippingTag, ShippingOption

pytestmark = pytest.mark.django_db


def test_shipping_options(product, basic_shipping_option):
    options = ShippingOption.objects.filter(shipping_tag=product.shipping_tag)
    assert options.count() == 1

