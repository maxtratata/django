from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddProductForm
from dz2.models import Client, Order,Product


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect(f'/order/order_cart')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('/cart')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})


def order_report(request, orders_30_days=None, orders_7_days=None, orders_365_days=None):
    # Нужно добавить фильтрацию
    clients = Client.objects.all()
    orders = Order.objects.all()
    products = Product.objects.all()
    return render(request, 'report/order.html', {'orders_7_days': orders_7_days,'orders_30_days': orders_30_days,
                                                 'orders_365_days': orders_365_days})
