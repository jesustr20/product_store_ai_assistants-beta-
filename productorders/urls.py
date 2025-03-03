from django.urls import path
from .views import (
    ProductOrdersCreateView,
    ProductOrdersListView,
    ProductOrdersDetailView,
    ProductOrdersUpdateView,
    ProductOrdersDestroyView
)

urlpatterns = [
    path('create', ProductOrdersCreateView.as_view(), name="productorder-create"),
    path('list', ProductOrdersListView.as_view(), name="productorder-list"),
    path('detail/<int:pk>/', ProductOrdersDetailView.as_view(), name="productorder-detail"),
    path('update/<int:pk>/', ProductOrdersUpdateView.as_view(), name="productorder-update"),
    path('delete/<int:pk>/', ProductOrdersDestroyView.as_view(), name="productorder-destroy"),
]