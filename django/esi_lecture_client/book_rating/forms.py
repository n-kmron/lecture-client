from django import forms
from .models import Book

class SearchBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title']