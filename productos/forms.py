from django import forms

from productos.models import *

class SeasonForm(forms.ModelForm):

    class Meta:
        model = Season
        fields = (
        'name',
        'background',

        )

class PricerForm(forms.ModelForm):

    class Meta:
        model = Pricer
        fields = (
        'size',
        'season',
        'product',
        'cant',
        )

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
        'upc',
        'name',
        'description',
        'price',
        'price_normal',
        'stock',
        )
