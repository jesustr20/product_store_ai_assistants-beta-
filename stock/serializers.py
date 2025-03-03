from rest_framework import serializers
from stock.models import Stock

class StockCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['amount']

class StockListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id','amount']

class StockDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id','amount']

class StockUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['amount']

class StockDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id','amount']