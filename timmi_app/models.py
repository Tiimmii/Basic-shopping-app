from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=3083)

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount=models.FloatField()