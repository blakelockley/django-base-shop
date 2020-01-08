from django.contrib import admin

from .models import (
    Address,
    Cart,
    CartItem,
    CheckoutDetails,
    Country,
    Order,
    OrderItem,
    Product,
    ShippingOption,
)


@admin.register(Address)
class Address(admin.ModelAdmin):
    pass


@admin.register(Cart)
class Cart(admin.ModelAdmin):
    pass


@admin.register(CartItem)
class CartItem(admin.ModelAdmin):
    pass


@admin.register(CheckoutDetails)
class CheckoutDetails(admin.ModelAdmin):
    pass


@admin.register(Country)
class Country(admin.ModelAdmin):
    pass


@admin.register(Order)
class Order(admin.ModelAdmin):
    pass


@admin.register(OrderItem)
class OrderItem(admin.ModelAdmin):
    pass


@admin.register(Product)
class Product(admin.ModelAdmin):
    search_fields = ("name", "part_number")
    filter_horizontal = ("images",)


@admin.register(ShippingOption)
class ShippingOption(admin.ModelAdmin):
    pass
