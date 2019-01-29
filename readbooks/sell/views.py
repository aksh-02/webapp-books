from django.shortcuts import render, redirect
from .models import Sold
from commerce.models import Product
from users.models import Profile
from cart.models import Cart, Bought
# Create your views here.

def sell_order(request):
	books = request.POST.getlist('book')
	buyer_name = request.POST.get('buyer')
	buyer_numb = request.POST.get('buyer_number')
	buyer_addr = request.POST.get('buyer_address')
	for bo in books:
		book = Product.objects.get(id=bo)

		obj = Sold()
		obj.book = book
		obj.seller = book.seller
		obj.seller_number = book.seller.profile.phone_number
		obj.seller_address = book.seller.profile.shipping_address
		obj.buyer = buyer_name
		obj.buyer_number = buyer_numb
		obj.buyer_address = buyer_addr
		obj.price = book.price
		obj.total = book.price
		obj.save()

		book.quantity = book.quantity - 1
		book.save()
		
		bou = Bought()
		bou.user = request.user
		bou.product = book.name
		bou.author = book.author
		bou.price = book.price
		bou.save()

	cart = Cart.objects.get(user=request.user)
	cart.products.clear()
	print('this is', cart)

	return redirect('cart:home')