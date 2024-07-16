from rest_framework import serializers
from .models import Category, Product, Brand, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'category', 'name', 'slug')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'slug', 'description', 'created_date', 'updated_date', 'price', 'min_order', 'brand', 'image', 'category')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'brand', 'product', 'count', 'arrive_date', 'market_id', 'status', 'created_date', 'updated_date')


