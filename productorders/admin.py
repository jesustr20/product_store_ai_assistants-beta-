from django.contrib import admin
from productorders.models import ProductOrder# Register your models here.

@admin.register(ProductOrder)
class ProductOrder(admin.ModelAdmin):
    list_display = ['amount']
