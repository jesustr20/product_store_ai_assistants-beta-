from django.urls import path
from .views import (
    OrderCreateView,
    OrderListView,
    OrderDetailView,
    OrderUpdateView,
    OrderDestroyView
)

urlpatterns = [
    path('create', OrderCreateView.as_view(), name="order-create"),
    path('list', OrderListView.as_view(), name="order-list"),
    path('detail/<int:pk>/', OrderDetailView.as_view(), name="order-detail"),
    path('update/<int:pk>/', OrderUpdateView.as_view(), name="order-update"),
    path('delete/<int:pk>/', OrderDestroyView.as_view(), name="order-destroy"),
]