from .models import Product
from django.forms import ModelForm
from django import forms


class BookOffer(ModelForm):

    # user = forms.CharField(disabled=True)

    class Meta:
        model = Product
        fields = ['title', 'author', 'price', 'condition']
        widgets = {'user': forms.HiddenInput}

