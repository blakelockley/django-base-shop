from django.db import models

from django_base_shop.models import BaseProduct, BaseOrder, BaseCheckoutDetails

class TestProduct(BaseProduct):
    pass

class TestOrder(BaseOrder):
    pass

class TestCheckoutDetails(BaseCheckoutDetails):
    pass