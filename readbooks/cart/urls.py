from django.urls import path
from .views import cart_home, cart_update, cart_order

urlpatterns = [
    path('', cart_home, name='home'),
    path('update/', cart_update, name='update'),
    path('order/', cart_order, name='order')
]