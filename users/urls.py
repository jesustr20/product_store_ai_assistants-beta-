from django.urls import path
from .views import (    
    UserCreateView,
    UserListView,
    UserDetailView,
    UserUpdateView,
    UserDestroyView
)

urlpatterns = [
    path('create', UserCreateView.as_view(), name="user-create"),
    path('list', UserListView.as_view(), name="user-list"),
    path('detail/<int:pk>/', UserDetailView.as_view(), name="user-detail"),
    path('update/<int:pk>/', UserUpdateView.as_view(), name="user-update"),
    path('delete/<int:pk>/', UserDestroyView.as_view(), name="user-destroy"),
]