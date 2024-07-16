from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=60)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Brand(models.Model):
    category = models.ForeignKey(Category, related_name='brands', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=60)
    image = models.ImageField(upload_to='products', blank=True)

    class Meta:
        verbose_name = 'Брэнд'
        verbose_name_plural = 'Брэнды'


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    # measurement = models.
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to='products', blank=True)
    slug = models.SlugField(max_length=50)
    min_order = models.IntegerField(default=1)
    brand = models.IntegerField(default=None)
    category = models.IntegerField(default=None)


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Order(models.Model):
    brand = models.IntegerField(default=None)
    product = models.IntegerField(default=None)
    count = models.IntegerField(default=1)
    arrive_date = models.DateTimeField(default=datetime.now, blank=True)
    market_id = models.IntegerField(default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
