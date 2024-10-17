from django import forms
from .models import Books, Category


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title',
                'author',
                'image',
                'photo_auther',
                'pages', 'price',
                'rental_price',
                'rental_period',                     
                'category',
                'status',
                'is_available'
                
                ]
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'photo_auther': forms.FileInput(attrs={'class':'form-control'}),
            'pages': forms.NumberInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'rental_price': forms.NumberInput(attrs={'class':'form-control'}),
            'rental_period': forms.NumberInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'}),
            'is_available': forms.CheckboxInput(attrs={'class':'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
        }