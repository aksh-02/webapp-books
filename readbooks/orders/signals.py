from django.db.models.signals import pre_save, post_save
from .models import Order
from cart.models import Cart
from django.dispatch import receiver


@receiver(pre_save, sender=Order)
def pre_save_order_id(sender, instance, *args, **kwargs):
	if not instance.order_id:
		instance.order_id = Order.update_order_id(instance)

@receiver(post_save, sender=Cart)
def post_save_total(sender, instance, *args, **kwargs):
	cart_obj = instance
	cart_id = cart_obj.id
	qs = Order.objects.filter(cart__id = cart_id)
	if qs.count() == 1:
		order_obj = qs.first()
		order_obj.update_total()

@receiver(post_save, sender=Order)
def post_save_order(sender, instance, created, *args, **kwargs):
	if created:
		instance.update_total()
