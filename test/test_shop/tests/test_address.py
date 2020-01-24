import pytest

pytestmark = pytest.mark.django_db


def test_address_formatted(shipping_address):

    expected = "123 Home Street\nSydney NSW 2000\nAustralia (Fixture)"
    assert shipping_address.formatted == expected
