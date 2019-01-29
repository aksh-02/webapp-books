from django.shortcuts import render, redirect
from .models import Cart, Bought
from commerce.models import Product
from orders.models import Order
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required()
def cart_home(request):
	#cart_obj, new = Cart.objects.new_or_get(request)
	cart_obj = Cart.objects.get(user=request.user)
	bought = Bought.objects.filter(user=request.user)
	#print('hello')
	#print(bought[0].product)
	context = {
		'cart' : cart_obj,
		'bought' : bought
	}
	return render(request, "cart/c_home.html", context)

def cart_update(request):
	print(request.POST)
	#cart_obj, new = Cart.objects.new_or_get(request)
	cart_obj = Cart.objects.get(user=request.user)
	product = Product.objects.get(id=request.POST.get('product_id'))
	if product in cart_obj.products.all():
		cart_obj.products.remove(product)
	else:
		cart_obj.products.add(product)
	return redirect('cart:home')

def cart_order(request):
	#cart_obj, new = Cart.objects.new_or_get(request)
	cart_obj = Cart.objects.get(user=request.user)
	cart_products = [i for i in cart_obj.products.all() if i.quantity != 0]	
	if cart_obj.products.count() == 0 or len(cart_products) == 0:  # deleted 'new or' 
		messages.success(request, f'No Books to CheckOut.  Please add some Books')
		return redirect('cart:home')
	else:
		order_obj, new_order = Order.objects.get_or_create(cart=cart_obj)
		books = [i.id for i in cart_obj.products.all() if i.quantity != 0]
		cart_books = [i for i in cart_obj.products.all() if i.quantity != 0]
		context = {
			'order': order_obj,
			'buyer': request.user,
			'books': books,
			'cart' : cart_obj,
			'cart_books' : cart_books,
		}
		print('ho')
		print(books)
		return render(request, 'cart/c_order.html', context)