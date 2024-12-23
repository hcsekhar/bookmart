from .models import food
from django import forms

class ProductFood(forms.ModelForm):
    class Meta:
        model = food
        fields= ['image', 'item_name', 'price', 'description','category']

