from django import forms
from .models import Order, Product


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image','price','quantity']