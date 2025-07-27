from django.db import models
from django.forms.models import ModelFormOptions


class Product(models.Model):
    """Товар"""
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    price = models.IntegerField(verbose_name="Цена")

    preview_img = models.ImageField(verbose_name="Превью картинка")

    bonus_count = models.IntegerField(verbose_name='количество бонусов', blank=True, null=True)
    # name = models.TextField(verbose_name='описание')
    old_price = models.IntegerField(verbose_name='старая цена', null=True, blank=True)

    is_on_sale = models.BooleanField(verbose_name='в наличии', default=False)
    weight = models.FloatField(verbose_name='вес', null=True, blank=True)
    country = models.CharField(verbose_name='страна производство', null=True, blank=True)
    brend = models.CharField(verbose_name='Бренд',null= True,blank=True)
    Product = models.IntegerField(verbose_name='artikul', null=True, blank=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['id']


class News(models.Model):
    """Новости"""
    nazvanie = models.CharField(verbose_name="название")
    data = models.CharField(verbose_name="название")
    opisanie = models.TextField(verbose_name="описание")
    photo = models.ImageField(verbose_name="сурот", null=True, blank=True)


class Car(models.Model):

    currency = [
        ("Сом", 'Сом'),
        ("Доллар", '$'),
    ]


    name = models.CharField()
    volume = models.FloatField()
    year = models.IntegerField()
    country = models.CharField()
    condition = models.CharField()
    gearbox = models.CharField()
    color = models.CharField()
    price = models.IntegerField()
    photo = models.ImageField()
    weight = models.FloatField()
    brand = models.CharField(default='mercedes')
    transmission = models.CharField()
    currency = models.CharField(verbose_name="Валюта", choices=currency, null=True, blank=True)

    class Meta:
        verbose_name = 'Моделька для машин'