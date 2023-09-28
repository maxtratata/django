from django.shortcuts import render
from dz2.models import Client, Order, Product


def order_report(request, orders_30_days=None, orders_7_days=None, orders_365_days=None):
    # Нужно добавить фильтрацию
    clients = Client.objects.all()
    orders = Order.objects.filter()
    products = Product.objects.all()
    return render(request, 'report/order.html', {'orders_7_days': orders_7_days,'orders_30_days': orders_30_days,
                                                 'orders_365_days': orders_365_days})
