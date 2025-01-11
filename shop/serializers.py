from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import Category, Product, CustomUser


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class ProductSerializer(serializers.ModelSerializer):
    category_name = SerializerMethodField('get_category_name')

    class Meta:
        model = Product
        fields = '__all__'

    def get_category_name(self, obj):
        return obj.category.name

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'phone_number',
            'first_name',
            'last_name',
            'profile_picture',
            'password'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = CustomUser(**validated_data)
        if password:

            user.set_password(password)
        user.save()
        return user
