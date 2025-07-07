from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Category, Product

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


# def men_list(request, slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True, gender='male')
    
#     if slug:
#         category = get_object_or_404(Category, slug=slug)
#         products = Product.objects.filter(category=category, gender='male')
    
#     return render(request, 'main/product/list_men.html',
#                   {'category':category,
#                    'categories':categories,
#                    'products':products,
#                    'slug_url': slug})

# def women_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True, gender='female')
    
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = Product.objects.filter(category=category, gender='female')
    
#     return render(request, 'main/product/list_women.html',
#                   {'category':category,
#                    'categories':categories,
#                    'products':products,
#                    'slug_url': category_slug})

def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)

    return render(request, 'main/product/detail.html', {'product':product})


def product_list(request, category_slug=None):
    page = request.GET.get('page', 1)
    category = None
    gender=None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    # paginator = Paginator(products, 10)
    # current_page = paginator.page(int(page))
    if 'women' in request.resolver_match.url_name:
        gender='female'
        products = products.filter(gender=gender)
    elif 'men' in request.resolver_match.url_name:
        gender='male'
        products = products.filter(gender=gender)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    paginator = Paginator(products, 10)
    current_page = paginator.page(int(page))

# сделай тут main/product/detail.html а второй product_list с main/index/index.html
# я редачила тут чтобы посмотреть что вышло
    return render(request, 'main/product/list.html',
                  {'category':category,
                   'categories':categories,
                   'products':current_page,
                   'slug_url': category_slug,
                   'gender':gender})