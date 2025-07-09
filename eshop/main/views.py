from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Category, Product
from cart.forms import CartAddProductForm



def index_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    
    return render(request, 'main/index/index.html',
                  {'category':category,
                   'categories':categories,
                   'products':products,
                   'slug_url': category_slug})

def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    cart_product_form = CartAddProductForm

    return render(request, 'main/product/detail.html', {'product':product,
                                                        'cart_product_form': cart_product_form})


def product_list(request, gender=None, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if gender:
        products = products.filter(gender=gender)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'main/product/list.html',
                  {'category':category,
                   'categories':categories,
                   'products':products,
                   'slug_url':category_slug,
                   'gender':gender})