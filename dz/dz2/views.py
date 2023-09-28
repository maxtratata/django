from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Product, Order, OrderItem
from .forms import OrderForm, ProductForm
from cart.forms import CartAddProductForm

from cart.cart import Cart


# Create your views here.
def client_detail(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'client/client_detail.html', {'client': client})


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client/client_list.html', {'clients': clients})


def create_client(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        client = Client.objects.create(name=name, email=email, phone_number=phone_number, address=address)
        return redirect(f'/client/{client.id}')

    return render(request, 'client/create_client.html')


def update_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        client.name = name
        client.email = email
        client.phone_number = phone_number
        client.address = address
        client.save()
        return render(request, 'success.html')

    return render(request, 'update_client.html', {'client': client})


def delete_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)

    if request.method == 'POST':
        client.delete()
        return render(request, 'success.html')

    return render(request, 'delete_client.html', {'client': client})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})


def product_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if "_update" in request.POST:
        return redirect(f'/product/{product.id}/update')

    if "_delete" in request.POST:
        return redirect(f'/product/{product.id}/delete')

    return render(request, 'product/product_view.html', {'product': product})


def product_detail(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            product = Product.objects.create(
                name=cd.get("name"),
                description=cd.get('description'),
                price=cd.get('price'),
                quantity=cd.get('quantity'),
                image=cd.get("image")
            )
            product.save()
            return redirect(f'/product/{product.id}')

    form = ProductForm(request.POST, request.FILES)
    return render(request, "product/product_detail.html", {'form': form})


def create_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        quantity = request.POST['quantity']
        product = Product.objects.create(name=name, description=description, price=price, quantity=quantity)
        return redirect(f'/product/{product.id}/update')

    return render(request, 'product/create_product.html')


def update_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = ProductForm(request.POST, request.FILES)

    if request.method == "POST":
        if form.is_valid():
            cd = form.cleaned_data

            for key, value in cd.items():
                setattr(product, key, value)
            product.save()
            return redirect(f'/product/{product.id}')

    form = ProductForm(initial={'name': product.name, 'description': product.description, 'price': product.price,
                                'quantity': product.quantity, 'image': product.image})
    return render(request, 'product/product_detail.html', {'form': form, 'product': product})


def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if product:
        product.delete()

    return redirect(f'/product/')


# Cписок всех заказов
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order/order_list.html', {'orders': orders})


# Создание нового заказа
def order_create(request):
    form = OrderForm()
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            client_id = form['client'].data

            if client_id:
                client = get_object_or_404(Client, id=client_id)
                order = Order.objects.create(client=client, total_amount=0)
                for item in cart:
                    OrderItem.objects.create(order=order,
                                             product=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'])
                cart.clear()
                return redirect(f'/')
    return render(request, 'order/order_create.html', {'form': form})


def order_cart(request):
    products = Product.objects.all()
    form = CartAddProductForm()
    # if request.method == 'POST':
    #     form = OrderCartForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('order_list')
    return render(request, 'order/order_cart.html', {'cart_product_form': form, "products": products})


# Просмотр информации о заказе
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order/order_detail.html', {'order': order})


# Обновление заказа
def order_update(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    return render(request, 'order/order_update.html', {'form': form, 'order': order})


# Удаление заказа
def order_delete(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'order/order_delete.html', {'order': order})


def index(request):
    clients = Client.objects.all()
    orders = Order.objects.all()
    products = Product.objects.all()
    return render(request, 'home/home.html', {'clients': clients, 'orders': orders, 'products': products})
