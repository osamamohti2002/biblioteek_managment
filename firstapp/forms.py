from django import forms
from .models import Books, Category


class BookForm(forms.ModelForm):
    class meta:
        model = Books
        fields = '__all__'

