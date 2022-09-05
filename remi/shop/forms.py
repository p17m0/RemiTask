from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('quantity', 'address',)
        labels = {
            'quantity': ('Количество товара'),
            'address': ('Адрес')
        }
        help_texts = {
            'address': ('Укажите полный адрес'),
        }
