from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import viewsets, permissions, filters
from rest_framework.generics import ListAPIView

from shop.models import Category, Product, CustomUser
from shop.serializers import CategorySerializer, ProductSerializer, CustomUserSerializer
from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    page_size = 10


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price', 'name']


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
