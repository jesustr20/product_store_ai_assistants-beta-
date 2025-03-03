from rest_framework import generics
from stock.models import Stock
from .serializers import (
    StockCreateSerializer,
    StockListSerializer,
    StockDetailSerializer,
    StockUpdateSerializer,
    StockDestroySerializer
)

# Create your views here.
class StockCreateView(generics.CreateAPIView):
    queryset = Stock.objects.all().order_by('id')
    serializer_class = StockCreateSerializer

class StockListView(generics.ListAPIView):
    queryset = Stock.objects.all().order_by('id')
    serializer_class = StockListSerializer

class StockDetailView(generics.RetrieveAPIView):
    queryset = Stock.objects.all().order_by('id')
    serializer_class = StockDetailSerializer

class StockUpdateView(generics.UpdateAPIView):
    queryset = Stock.objects.all().order_by('id')
    serializer_class = StockUpdateSerializer

class StockDestroyView(generics.DestroyAPIView):
    queryset = Stock.objects.all().order_by('id')
    serializer_class = StockDestroySerializer
