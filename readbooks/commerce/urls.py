from django.urls import path
from .views import add_book, CommerceHome, BookView


urlpatterns = [
	path('', CommerceHome.as_view(), name='commerce-home'),
	path('book/register/', add_book, name='register-book'),
	path('bookview/<str:slug>', BookView.as_view(), name='book-view'),
]