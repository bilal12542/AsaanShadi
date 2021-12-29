from django import forms
from .models import Product, Images


class AddProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'tags', 'quantity', 'price', 'image']


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Images
        fields = ('image',)

