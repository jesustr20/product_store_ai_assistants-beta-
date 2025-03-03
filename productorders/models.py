from django.db import models
from orders.models import Order
from products.models import Product

# Create your models here.
class ProductOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='productorders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='productorders')
    amount = models.PositiveIntegerField()