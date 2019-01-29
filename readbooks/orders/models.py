from django.db import models
from cart.models import Cart
import random, string

# Create your models here.
class Order(models.Model):
	order_id = models.CharField(max_length=10, blank=True)
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	sub_total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

	def __str__(self):
		return self.order_id
	
	def update_order_id(self):
		if not self.order_id:
			size = 10
			opts = string.ascii_lowercase + string.digits
			o_id = "".join(random.choice(opts) for _ in range(size)).upper()
			while Order.objects.filter(order_id = o_id).exists():
				o_id = "".join(random.choice(string.digits + string.ascii_lowercase) for _ in range(size)).upper()
			return o_id
	
	def update_total(self):
		self.sub_total = self.cart.total
		self.total = self.sub_total + 50
		self.save()