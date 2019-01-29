from django import forms
from .models import Product, Genre


class BookForm(forms.ModelForm):
	genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), widget=forms.CheckboxSelectMultiple(), required=False)
	
	class Meta:
		model = Product
		fields = ['name', 'author', 'genre', 'description', 'price', 'quantity', 'image']