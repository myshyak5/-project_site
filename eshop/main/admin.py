from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'gender', 'size', 'available',
                    'created', 'updated', 'discount']
    list_filter = ['available', 'gender', 'size']
    list_editable = ['price', 'available', 'discount']
    prepopulated_fields = {'slug': ('name',)}