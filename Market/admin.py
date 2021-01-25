from django.contrib import admin
from Users.models import User
from Market.models import Product, Opinion, Order


# Register your models here.
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Opinion)
admin.site.register(Order)
