from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from seller.models import Product

# Create your models here.

class Costumer(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    password = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.firstName + " " + self.lastName

class Cart(models.Model):
    buyer = models.ForeignKey(Costumer, on_delete=models.CASCADE, default='')
    products = models.ForeignKey(Product, on_delete=models.CASCADE, default='')

    # def __str__(self):
    #     return self.buyer.firstName + ' ' + self.products.name
