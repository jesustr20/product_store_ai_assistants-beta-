from django.urls import path
from .views import (
    ProductCreateView,
    ProductListView,
    ProductDetailView,
    ProductUpdateView,
    ProductDestroyView
)

urlpatterns = [
    path('create', ProductCreateView.as_view(), name="product-create"),
    path('list', ProductListView.as_view(), name="product-list"),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name="product-detail"),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name="product-update"),
    path('delete/<int:pk>/', ProductDestroyView.as_view(), name="product-destroy"),
]