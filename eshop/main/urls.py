from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
     path('', views.index_list, name='index_list'),
     path('shop/men/category/<slug:category_slug>/', views.product_list, name='product_list_men_by_category'),
     path('shop/women/category/<slug:category_slug>/', views.product_list, name='product_list_women_by_category'),
     path('shop/men/', views.product_list, name='product_list_men'),
     path('shop/women/', views.product_list, name='product_list_women'),
     path('shop/category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
     path('shop/<slug:slug>/', views.product_details, name='product_detail'),
     path('shop/', views.product_list, name='product_list'),
     
]