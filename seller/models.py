# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Sell(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    password = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.firstName + " " + self.lastName


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.BinaryField(max_length=100)
    price = models.IntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    seller = models.ForeignKey(Sell, on_delete=models.CASCADE, default='')

    # def __str__(self):
    # return self.name + ' ' + self.description
