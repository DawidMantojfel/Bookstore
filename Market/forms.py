from .models import Product
from django.forms import ModelForm
from django import forms


class BookOffer(ModelForm):


    class Meta:
        model = Product
        fields = ['title', 'author', 'price', 'condition', 'image']
        widgets = {'user': forms.HiddenInput, 'image': forms.HiddenInput}

