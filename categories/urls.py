from django.urls import path
from .views import (
    CategoryCreateView,
    CategoryListView,
    CategoryDetailView,
    CategoryUpdateView,
    CategoryDestroyView
)

urlpatterns = [
    path('create', CategoryCreateView.as_view(), name="category-create"),
    path('list', CategoryListView.as_view(), name="category-list"),
    path('detail/<int:pk>/', CategoryDetailView.as_view(), name="category-detail"),
    path('update/<int:pk>/', CategoryUpdateView.as_view(), name="category-update"),
    path('delete/<int:pk>/', CategoryDestroyView.as_view(), name="category-destroy"),
]