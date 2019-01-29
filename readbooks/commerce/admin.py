from django.contrib import admin
from .models import Product, Genre
from .forms import BookForm

# Register your models here.
admin.site.register(Product)
admin.site.register(Genre)
