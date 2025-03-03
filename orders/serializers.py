from rest_framework import serializers
from orders.models import Order

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['fecha', 'total']

class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','fecha', 'total']

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','fecha', 'total']

class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['fecha', 'total']

class OrderDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','fecha', 'total']