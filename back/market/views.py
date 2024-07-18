from rest_framework import viewsets
from .models import Category, Brand, Product, Order
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer, OrderSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.response import Response
from rembg import remove
import os
from pathlib import Path
from datetime import datetime
from slugify import slugify
import json


BASE_DIR = Path(__file__).resolve().parent.parent

def rembg_img(img):
    input_path = img
    date_now = datetime.now().microsecond
    output_path = f"{os.path.join(BASE_DIR, 'products/')}{date_now}_{str(input_path)}"
    with open(output_path, 'wb') as o:
        input = input_path.read()
        output = remove(input)
        o.write(output)
        return f"{date_now}_{str(input_path)}"


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        name = request.data['name']
        slug = slugify(name)
        Category.objects.create(name=name, slug=slug)
        return Response('Category saved', status=status.HTTP_201_CREATED)


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        name = request.data['name']
        description = request.data['description']
        price = request.data['price']
        slug = slugify(name)
        min_order = request.data['min_order']
        brand_id = 1
        category_id = request.data['category']
        image = request.data['image']
        img = rembg_img(image)
        Product.objects.create(name=name, description=description, price=price, min_order=min_order, slug=slug, image=img, brand=brand_id, category=category_id)
        return Response('Product saved', status=status.HTTP_201_CREATED)
    
    def partial_update(self, request, *args, **kwargs):
        id = request.data['id']
        name = request.data['name']
        description = request.data['description']
        price = request.data['price']
        image = request.data['image']
        if type(image) == str:
            img = image.split('products/')[-1]
        else:
            img = rembg_img(image)
        slug = slugify(name)
        item = Product.objects.get(pk=id)
        item.name = name
        item.description = description
        item.price = price
        item.image = img
        item.slug = slug
        item.save(update_fields=['name', 'description', 'price', 'image', 'slug'])
        return Response('Product changed', status=status.HTTP_200_OK)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.filter()
    serializer_class = OrderSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser)

    def list(self, request):
        result = []
        orders = Order.objects.filter(brand=1).values()
        for order in orders:
            product = Product.objects.filter(id=order['product']).values()
            res = {
                'id': order['id'],
                'product': product[0]['name'],
                'image': product[0]['image'],
                'count': order['count'],
                'market': 'маг. Тест',
                'market_address': 'Тест 55',
                'market_contact': '+77786768246',
                'created_date': order['created_date'],
                'updated_date': order['updated_date'],
                'status': order['status']
            }
            result.append(res)
        return Response(result)

