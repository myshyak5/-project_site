from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)

    return render(request, 'main/product/detail.html', {'product':product})



# def index_list(request, slug):
#     product = get_object_or_404(Product, slug=slug, available=True)

#     return render(request, 'main/index/index.html', {'product':product})
