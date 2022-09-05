from django import forms
from django.core.exceptions import ValidationError

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

    def clean_quantity(self):
        data = self.cleaned_data['quantity']
        if data > 100:
            raise ValidationError('Не многовато ли?')
        return data
