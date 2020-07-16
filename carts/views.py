from django.shortcuts import render

from .models import Cart

def cart_home(request):
    cart_id = Cart.objects.get_or_new(request)
    return render(request, "carts/home.html", {})