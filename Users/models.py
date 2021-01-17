from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    OPINION_CHOICES = (
        ('negative', 'negative'),
        ('neutral', 'neutral'),
        ('good', 'good'),
    )
    # opinion = models.CharField(max_length=1000, choices=OPINION_CHOICES)
