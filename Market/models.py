from django.db import models
from Users.models import User


class Product(models.Model):
    CONDITION_CHOICES = (
        ('bad', 'bad'),
        ('used', 'used'),
        ('new', 'new'),
    )
    # who is selling book
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # book title
    title = models.CharField(max_length=100, null=True)
    # book author
    author = models.CharField(max_length=100, null=True)
    # book description
    description = models.CharField(max_length=5000, null=True, blank=True)
    # book image
    image = models.URLField(blank=True, null=True)
    # price of the book
    price = models.FloatField()
    condition = models.CharField(max_length=4, choices=CONDITION_CHOICES)
    # when the book was added
    date = models.DateTimeField(auto_now_add=True, null=True)
    # is the book already sold
    sold = models.BooleanField(default=False)
    # you can rate the book added in market

    def __str__(self):
        return f"book: {self.title} \n " \
               f"seller: {self.user}"


class Opinion(models.Model):
    '''kto wystawil, komu i tresc'''
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, default=None)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return f"Opinion By '{self.user}' on '{self.product}'"


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=True, default=None)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
