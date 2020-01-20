from django.http import HttpResponse
from .models import ConcreteCart, ConcreteProduct


def index(request):
    return HttpResponse(b"Hello world")


def check_cart(request):
    cart = request.cart

    if not cart.is_persisted:
        return HttpResponse(b"None")

    return HttpResponse(cart.cart_token.encode("utf-8"))


def check_cart_items(request):
    cart = request.cart

    if not cart.is_persisted:
        return HttpResponse(b"None")

    body = f"{cart.cart_token}<br /><br />"
    for item in cart.items.all():
        body += f"{item.product.name} {item.quantity}<br />"

    return HttpResponse(body.encode("utf-8"))


def add_cart_item(request, pk):
    cart = request.cart

    if ConcreteProduct.objects.count() == 0:
        ConcreteProduct.objects.create(handle="ANV-001", name="Anvil", price=100.0)

    product = ConcreteProduct.objects.get(pk=pk)
    cart.add_item(product, 1)

    return HttpResponse(b"Item added! <a href='/check_cart_items'>Check items</a>")


def remove_cart_item(request, pk):
    cart = request.cart

    product = ConcreteProduct.objects.get(pk=pk)
    cart.remove_item(product)

    return HttpResponse(b"Item removed! <a href='/check_cart_items'>Check items</a>")
