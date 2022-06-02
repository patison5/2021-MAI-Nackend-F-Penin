from statistics import mode
import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Product, Category


# class CategorytModel:
#     def __init__(self, category_text) -> None:
#         self.category_text = category_text


class CategorySerializer(serializers.Serializer):
    category_text = serializers.CharField(max_length=200)
        
# def encode():
#     model = CategorytModel('category_text value')
#     model_sr = CategorySerializer(model)
#     print(model_sr.data, type(model_sr.data), sep="\n")
#     json = JSONRenderer().render(model_sr.data)
#     print(json)

# def decode():
#     stream = io.BytesIO(b'{"category_text":"category_text value"}')
#     data = JSONParser().parse(stream)
#     serializer = CategorySerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)