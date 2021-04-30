from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def process(request):
    product = Product.objects.get(id=(request.POST["id"]))
    quantity_from_form = int(request.POST["quantity"])
    price = product.price
    total_charge = quantity_from_form * price
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect("amadon/checkout")

def confirmation(request):
    last_ordered = Order.objects.last()
    orders = Order.objects.all()
    context = {
        "last_ordered": last_ordered,
    }
    return render(request, "store/checkout.html", context)