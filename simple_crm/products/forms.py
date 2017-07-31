from django import forms
from .models import Products, Editions

class CreateForm(forms.ModelForm):
    name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = Products
        fields = ('name', 'sku', 'vendor', 'price_per', 'price', 'monthly_price', 'yearly_price', 'tags', 'description', )

