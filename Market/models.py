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
    # book title
    title = models.CharField(max_length=500, null=True)
    # book author
    author = models.CharField(max_length=500, null=True)
    # book description
    description = models.CharField(max_length=5000, null=True, blank=True)
    # book image
    image = models.URLField(blank=True, null=True)
    # price of the book
    price = models.FloatField()
    condition = models.CharField(max_length=4, choices=CONDITION_CHOICES)
    # when the book was added
    date = models.DateTimeField(auto_now_add=True, null=True)
    # you can rate the book added in market

    def __str__(self):
        return f"BOOK: {self.title} \n SELLER: {self.user}"


# class Opinion(models.Model):
#     '''kto wystawil, komu i tresc'''
#     # product that opinion is related to
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, default=None)
#     # owner of the product
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     # opinion maker
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
#     # content of opinion
#     content = models.CharField(max_length=2000, null=True)
#
#     def __str__(self):
#         return f"Opinion By '{self.customer}' on '{self.product}'"
#
#
# class Customer(models.Model):
#     # every customer must be a user
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#     name = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)
#
#     def __str__(self):
#         return self.name


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


class ShippingAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zip_code = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Shipping Addresses"

    def __str__(self):
        return self.address


# This is class of a Book for storage and saving to database.
class BookModel:
    def __init__(self, id, authors, title, description, image=None):
        self.id = id
        self.authors = authors
        self.title = title
        self.image = image
        self.description = description

    def __str__(self):
        return f'{self.image}'
