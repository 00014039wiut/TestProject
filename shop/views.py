from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import viewsets, permissions
from rest_framework.generics import ListAPIView

from shop.models import Category, Product, CustomUser
from shop.serializers import CategorySerializer, ProductSerializer, CustomUserSerializer


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
