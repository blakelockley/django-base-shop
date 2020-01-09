from django.http import HttpResponse
from .models import ConcreteCart


def index(request):
    return HttpResponse(b"Hello world")


def create_cart(request):
    cart = ConcreteCart.objects.create()

    response = HttpResponse(status=204)
    response.set_cookie("cart_token", cart.cart_token)

    return response


def check_cart(request):
    cart = request.cart

    if cart is None:
        return HttpResponse(b"None")

    return HttpResponse(cart.cart_token.encode("utf-8"))
