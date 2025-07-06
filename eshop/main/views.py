from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)

    return render(request, 'main/product/detail.html', {'product':product})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

# сделай тут main/product/detail.html а второй product_list с main/index/index.html
# я редачила тут чтобы посмотреть что вышло
    return render(request, 'main/index/index.html',
                  {'category':category,
                   'categories':categories,
                   'products':products})