from .models import Cart


class CartMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Before view
        cart_token = request.COOKIES.get("cart_token")
        if cart_token:
            request.cart = Cart.objects.filter(cart_token=cart_token).first()

        # Response
        response = self.get_response(request)
        return response
