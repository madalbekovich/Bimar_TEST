from django.shortcuts import render
from . import serializers, models
from rest_framework import generics


class ProductListView(generics.ListAPIView):
    """Представление для списка продуктов"""
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class NewsListView(generics.ListAPIView):
    """Представление для списка новости"""
    queryset = models.News.objects.all()
    serializer_class = serializers.NewSerializer
