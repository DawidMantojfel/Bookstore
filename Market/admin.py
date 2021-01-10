from django.contrib import admin
from Users.models import User
from Market.models import Book, Market, Opinion


# Register your models here.
admin.site.register(Book)
admin.site.register(Market)
admin.site.register(User)
admin.site.register(Opinion)
