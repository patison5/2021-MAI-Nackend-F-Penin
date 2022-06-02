from urllib.request import Request
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import Product, Category
from .Serializers import CategorySerializer
    
class ProductAPIView(APIView):
    
    def get(self, request):
        lst = Product.objects.all().values()
        return Response({'data': list(lst)})
    
    def post(self, request):
        product_new = Product.objects.create(
            product_title=request.data['product_title'],
            product_text=request.data['product_text'],
            product_price=request.data['product_price']
        )
        
        return Response({'data': model_to_dict(product_new)})
    
    
class CategoryAPIView(APIView):
    
    def get(self, request):        
        lst = Category.objects.all()
        return Response({'data': CategorySerializer(lst, many=True).data})

    def post(self, request):
        # serializer = CategorySerializer(data=request.data)
        # k = serializer.is_valid(raise_exception=True)
        # print(k)
        
        category_new = Category.objects.create(
            category_text=request.data['category_name']
        )
        
        return Response({'data': CategorySerializer(category_new).data})