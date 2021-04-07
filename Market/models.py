from django.db import models
from Users.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Product(models.Model):
    CONDITION_CHOICES = (
        ('bad', 'bad'),
        ('used', 'used'),
        ('new', 'new'),
    )
    # who is selling book
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # how many books you have for sell
    quantity = models.SmallIntegerField(null=False, default=1)
    title = models.CharField(max_length=500, null=True)
    author = models.CharField(max_length=500, null=True)
    description = models.CharField(max_length=5000, null=True, blank=True)
    image = models.URLField(blank=True, null=True)
    # price of the book
    price = models.FloatField()
    condition = models.CharField(max_length=4, choices=CONDITION_CHOICES)
    infolink = models.URLField(blank=True, null=True)
    # when the book was added
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"BOOK: {self.title} \n SELLER: {self.user}"


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    # who is buying product
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True, null=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return f"CUSTOMER: {self.customer} COMPLETED: {self.complete} ID: {self.transaction_id}"


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.product) + '|' + f"{self.order}"


# class ShippingAddress(models.Model):
#     customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
#     address = models.CharField(max_length=200, null=True)
#     city = models.CharField(max_length=200, null=True)
#     state = models.CharField(max_length=200, null=True)
#     zip_code = models.CharField(max_length=200, null=True)
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         verbose_name_plural = "Shipping Addresses"
#
#     def __str__(self):
#         return self.address



