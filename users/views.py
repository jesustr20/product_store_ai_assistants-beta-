from rest_framework import generics
from users.models import User
from .serializers import (
    UserCreateSerializer, 
    UserDetailSerializer, 
    UserListSerializer, 
    UserUpdateSerializer,
    UserDestroySerializer)

# Create your views here.

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserCreateSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserListSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserDetailSerializer

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserUpdateSerializer

class UserDestroyView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer