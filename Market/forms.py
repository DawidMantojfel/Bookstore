from .models import Market
from django.forms import ModelForm


class BookOffer(ModelForm):
    class Meta:
        model = Market
        fields = ['book', 'price', 'condition']
