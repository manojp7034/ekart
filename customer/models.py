from django.db import models
from seller.models import Product

# Create your models here.
class Customer(models.Model):
    name=models.TextField(max_length=100,null=True)
    email=models.TextField(max_length=100,null=True)
    password=models.TextField(max_length=100,null=True)

class Cart(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    product=models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity=models.PositiveIntegerField(default=1)