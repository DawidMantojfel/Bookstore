from .models import Product
from django.forms import ModelForm
from django import forms


class BookOffer(ModelForm):
    quantity = forms.IntegerField(min_value=1, max_value=100)
    price = forms.FloatField(min_value=1, max_value=10000)

    class Meta:
        model = Product
        fields = ['title', 'author', 'price', 'condition', 'image', 'quantity']
        widgets = {'user': forms.HiddenInput, 'image': forms.HiddenInput}

