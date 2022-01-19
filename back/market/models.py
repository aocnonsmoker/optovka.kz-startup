from django.db import models
from django.contrib.auth.models import User


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
    brand = models.ForeignKey(Brand, related_name='orders', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Order(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
