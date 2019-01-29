from django.db import models
from commerce.models import Product

# Create your models here.
class Sold(models.Model):
	book = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1, blank=True, null=True)
	seller = models.CharField(max_length=50)
	seller_number = models.CharField(max_length=50)
	seller_address = models.TextField()
	buyer = models.CharField(max_length=50)
	buyer_number = models.CharField(max_length=50)
	buyer_address = models.TextField()
	price = models.DecimalField(null=True, blank=True, max_digits=100, decimal_places=2)
	total = models.DecimalField(null=True, blank=True, max_digits=100, decimal_places=2)
	date_sold = models.DateTimeField(auto_now_add=True)    
	delivered = models.BooleanField(default=False, blank=True)

	def __str__(self):
		return f'{self.book} by {self.seller} to {self.buyer}'

	def __unicode__(self):
		return f'{self.book} by {self.seller} to {self.buyer}'
