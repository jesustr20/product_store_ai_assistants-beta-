from rest_framework import generics
from products.models import Product
from .serializers import (
    ProductCreateSerializer,
    ProductListSerializer,
    ProductDetailSerializer,
    ProductUpdateSerializer,
    ProductDestroySerializer
)

# Create your views here.
class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductCreateSerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductListSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductDetailSerializer

class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductUpdateSerializer

class ProductDestroyView(generics.DestroyAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductDestroySerializer
