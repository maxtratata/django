from django import forms

from cart.cart import Cart

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class Cart(forms.Form):
    class Meta:
        model = Cart
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "description")