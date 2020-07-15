from django.shortcuts import render

def cart_home(request):
    cart_id = request.session.get('cart_id', None)
    if cart_id is not None:
        print("new cart created")
        request.session["cart_id"] = 12
    else:
        print("Cart id is exists.")
    return render(request, "carts/home.html", {})