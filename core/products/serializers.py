from rest_framework import serializers
from . import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = ['nazvanie', 'opisanie', 'photo', 'data']


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Car
        # fields = ['name', 'volume', 'country', 'brand', 'transmission', 'weight', 'price', 'gearbox', 'color']
        fields = '__all__'
