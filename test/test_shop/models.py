from django.db import models

from django_base_shop.models import (
    BaseCart,
    BaseCartItem,
    BaseCheckoutDetails,
    BaseOrder,
    BaseOrderItem,
    BaseProduct,
)


class ConcreteProduct(BaseProduct):
    pass


class ConcreteOrderItem(BaseOrderItem):
    pass


class ConcreteOrder(BaseOrder):
    pass


class ConcreteCheckoutDetails(BaseCheckoutDetails):
    pass


class ConcreteCartItem(BaseCartItem):
    pass


class ConcreteCart(BaseCart):
    pass
