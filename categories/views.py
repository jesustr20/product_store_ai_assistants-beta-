from rest_framework import generics
from categories.models import Category
from .serializers import (
    CategoryCreateSerializer,
    CategoryListSerializer,
    CategoryDetailSerializer,
    CategoryUpdateSerializer,
    CategoryDestroySerializer
)

# Create your views here.
class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategoryCreateSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategoryListSerializer

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategoryDetailSerializer

class CategoryUpdateView(generics.UpdateAPIView):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategoryUpdateSerializer

class CategoryDestroyView(generics.DestroyAPIView):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategoryDestroySerializer
