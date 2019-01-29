from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Product
from cart.models import Cart


@receiver(post_save, sender=Product)
def upd_cart_total(sender, instance, created, **kwargs):
	if not created:
		for obj in instance.cart_set.all():
			obj.upd_total()
