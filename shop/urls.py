from django.urls import path
from rest_framework.routers import DefaultRouter
from shop import views

# Initialize the router for the shop app
router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'products', views.ProductViewSet, basename='product')
router.register(r'users', views.UserViewSet, basename='user')

# Define app-specific urlpatterns
urlpatterns = router.urls
