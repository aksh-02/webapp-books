from django.dispatch import receiver
from .models import Cart, Bought
from django.db.models.signals import m2m_changed, post_save
from django.contrib.auth.models import User

@receiver(m2m_changed, sender=Cart.products.through)
def cart_total(sender, instance, action, *args, **kwargs):
	if action in ['post_add', 'post_remove', 'post_clear']:
		products = instance.products.all()
		total = 0
		for x in products:
			if x.quantity != 0:
				total += x.price
		instance.total = total
		print(total)
		instance.save()

@receiver(post_save, sender=User)
def cart_create(sender, instance, created, *args, **kwargs):
	if created:
		Cart.objects.create(user=instance)