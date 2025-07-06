from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
     path('', views.index_list, name='index_list'),
     path('shop/', views.product_list, name='product_list'),
     path('shop/<slug:slug>/', views.product_details, name='product_detail'),
     path('shop/category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
     path('shop/men/<slug:slug>/', views.men_list, name='men_list'),
     path('shop/women/<slug:slug>/', views.women_list, name='women_list'),
]
