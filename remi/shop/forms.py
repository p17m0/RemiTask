from django import forms

from .models import BasketItem, Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
