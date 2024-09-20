from django.db import models
from . models import*

# Create your models here.
class Seller(models.Model):
    name=models.TextField(max_length=100, null=True)
    email=models.TextField(max_length=100,null=True)
    password=models.TextField(max_length=100,null=True)
class Product(models.Model):
    name=models.TextField(max_length=100, null=True)
    price=models.FloatField(null=True)
    description=models.TextField(max_length=400, null=True)
    image=models.ImageField(upload_to='product', null=True)