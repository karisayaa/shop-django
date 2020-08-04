from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    rating = models.DecimalField(max_digits=10, decimal_places=2)
