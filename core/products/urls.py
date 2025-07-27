from django.urls import path
from . import views

urlpatterns = [
    path('product-list/', views.ProductListView.as_view()),
    path('news-list/', views.NewsListView.as_view()),
    path('car-list/', views.CarListView.as_view()),
]