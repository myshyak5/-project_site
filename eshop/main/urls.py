from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
     path('', views.index_list, name='index_list'),
     path('<slug:slug>/', views.product_details,
          name='product_detail')
]
