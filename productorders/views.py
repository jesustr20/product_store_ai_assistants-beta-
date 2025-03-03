from rest_framework import generics
from productorders.models import ProductOrder
from .serializers import (
    ProductOrdersCreateSerializer,
    ProductOrdersListSerializer,
    ProductOrdersDetailSerializer,
    ProductOrdersUpdateSerializer,
    ProductOrdersDestroySerializer
)

# Create your views here.
class ProductOrdersCreateView(generics.CreateAPIView):
    queryset = ProductOrder.objects.all().order_by('id')
    serializer_class = ProductOrdersCreateSerializer

class ProductOrdersListView(generics.ListAPIView):
    queryset = ProductOrder.objects.all().order_by('id')
    serializer_class = ProductOrdersListSerializer

class ProductOrdersDetailView(generics.RetrieveAPIView):
    queryset = ProductOrder.objects.all().order_by('id')
    serializer_class = ProductOrdersDetailSerializer

class ProductOrdersUpdateView(generics.UpdateAPIView):
    queryset = ProductOrder.objects.all().order_by('id')
    serializer_class = ProductOrdersUpdateSerializer

class ProductOrdersDestroyView(generics.DestroyAPIView):
    queryset = ProductOrder.objects.all().order_by('id')
    serializer_class = ProductOrdersDestroySerializer
