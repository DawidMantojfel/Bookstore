from django.contrib import admin
from Users.models import User
from Market.models import Product, Order, OrderItem, ShippingAddress


# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
