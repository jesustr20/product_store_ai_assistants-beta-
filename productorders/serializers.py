from rest_framework import serializers
from productorders.models import ProductOrder

class ProductOrdersCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = ['amount']

class ProductOrdersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = ['id', 'amount']

class ProductOrdersDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = ['id', 'amount']

class ProductOrdersUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = ['amount']

class ProductOrdersDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = ['id', 'amount']