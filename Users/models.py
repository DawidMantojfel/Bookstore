from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    rate = models.FloatField(null=True)


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    e_mail = models.EmailField(max_length=30)


class Market(models.Model):
    CONDITION_CHOICES = (
        ('bad', 'bad'),
        ('used', 'used'),
        ('new', 'new'),
    )

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    price = models.FloatField()
    sold = models.BooleanField(default=False)
    condition = models.CharField(max_length=4, choices=CONDITION_CHOICES)
    date = models.DateTimeField(auto_now_add=True)


class Opinion(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    opinion = models.CharField(max_length=2000)
