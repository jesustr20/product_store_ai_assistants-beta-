from django.urls import path
from .views import (
    StockCreateView,
    StockListView,
    StockDetailView,
    StockUpdateView,
    StockDestroyView
)

urlpatterns = [
    path('create', StockCreateView.as_view(), name="stock-create"),
    path('list', StockListView.as_view(), name="stock-list"),
    path('detail/<int:pk>/', StockDetailView.as_view(), name="stock-detail"),
    path('update/<int:pk>/', StockUpdateView.as_view(), name="stock-update"),
    path('delete/<int:pk>/', StockDestroyView.as_view(), name="stock-destroy"),
]