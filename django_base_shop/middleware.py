from django.apps import apps
from django.conf import settings

Cart = apps.get_model(settings.SHOP_CART_MODEL)


class CartMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Request
        cart_token = request.COOKIES.get("cart_token")
        if cart_token:
            request.cart = Cart.objects.filter(cart_token=cart_token).first()
        else:
            request.cart = None

        # Response
        response = self.get_response(request)
        return response
