from django.db import models
from products.models import Product

# Create your models here.
class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="stock")
    amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.amount} - {self.amount}"