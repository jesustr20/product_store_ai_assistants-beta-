from django.contrib import admin
from stock.models import Stock
# Register your models here.

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['amount']
