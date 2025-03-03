from rest_framework import generics
from orders.models import Order
from .serializers import (
    OrderCreateSerializer,
    OrderListSerializer,
    OrderDetailSerializer,
    OrderUpdateSerializer,
    OrderDestroySerializer
)

# Create your views here.
class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderCreateSerializer

class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderListSerializer

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderDetailSerializer

class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderUpdateSerializer

class OrderDestroyView(generics.DestroyAPIView):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderDestroySerializer
