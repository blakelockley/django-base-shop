from django.db import models

from django_base_shop.models import (
    BaseCart,
    BaseCartItem,
    BaseCheckoutDetails,
    BaseOrder,
    BaseOrderItem,
    BaseProduct,
)


class TestProduct(BaseProduct):
    pass


class TestOrderItem(BaseOrderItem):
    pass


class TestOrder(BaseOrder):
    pass


class TestCheckoutDetails(BaseCheckoutDetails):
    pass


class TestCartItem(BaseCartItem):
    pass


class TestCart(BaseCart):
    pass
