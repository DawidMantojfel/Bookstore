from django.db import models
from Users.models import User
# Create your models here.
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    rate = models.FloatField(null=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    description = models.CharField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"


class Market(models.Model):
    CONDITION_CHOICES = (
        ('bad', 'bad'),
        ('used', 'used'),
        ('new', 'new'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    price = models.FloatField()
    condition = models.CharField(max_length=4, choices=CONDITION_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return f"book: {self.book} \n " \
               f"seller: {self.user}"


class Opinion(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    opinion = models.CharField(max_length=2000)

    def __str__(self):
        return f"Opinion By '{self.user}' on '{self.book}'"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
