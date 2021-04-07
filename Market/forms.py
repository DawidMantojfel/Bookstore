from .models import Product
from django.forms import ModelForm
from django import forms


# This is class of a Book for storage and saving to database.
class BookModel:
    def __init__(self, id, authors, title, description, infolink, image=None):
        self.id = id
        self.authors = authors
        self.title = title
        self.image = image
        self.infolink = infolink
        self.description = description

    def __str__(self):
        return f'{self.image}'


class BookOffer(ModelForm):
    quantity = forms.IntegerField(min_value=1, max_value=100)
    price = forms.FloatField(min_value=1, max_value=10000)

    class Meta:
        model = Product
        fields = ['price', 'condition', 'quantity', 'author', 'title']
        widgets = {
            'user': forms.HiddenInput,
            'author': forms.HiddenInput,
            'title': forms.HiddenInput,
        }

