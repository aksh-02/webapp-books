from django.db import models
from django.contrib.auth.models import User
from commerce.models import Product
#from django.conf import settings
#User = settings.AUTH_USER_MODEL

# Create your models here.
class CartManager(models.Manager):
	def new_or_get(self, request):
		cart_id =request.session.get("cart_id")
		qs = Cart.objects.filter(id=cart_id)
		if qs.count() == 1:
			cart_obj = qs.first()
			new_obj = False
			if request.user.is_authenticated and cart_obj.user is None:
				cart_obj.user = request.user
				cart_obj.save()
			print('cart exists', cart_id)
		else:
			if request.user.is_authenticated:
				cart_obj = Cart.objects.new(user=request.user)
			else:
				cart_obj = Cart.objects.new()
			request.session['cart_id'] = cart_obj.id
			new_obj = True
			print('new cart created')
		return cart_obj, new_obj

	def new(self, user=None):
		user_obj = user
		if user is not None and user.is_authenticated:
			user_obj = user
		return self.model.objects.create(user=user_obj)


class Cart(models.Model):
	#user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	products = models.ManyToManyField(Product, blank=True)
	total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	c_created = models.DateTimeField(auto_now_add=True)
	c_updated = models.DateTimeField(auto_now=True)

	objects = CartManager()
	def __str__(self):
		return str(self.id)

	def upd_total(self):
		tot = 0
		for i in self.products.all():
			if i.quantity != 0:
				tot += i.price
		self.total = tot
		self.save()

class Bought(models.Model):
	STATUS_CHOICES = (('Delivered', 'Delivered'), ('Shipped', 'Shipped'))

	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	product = models.CharField(max_length=100, blank=True, null=True)
	author = models.CharField(max_length=100, blank=True)
	price = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	quantity = models.IntegerField(default=1)
	status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Shipped', blank=True)
	bought = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.id)
