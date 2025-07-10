from django.db import models
from django.urls import reverse

GENDER = [('Женский', 'Женский'), ('Мужской', 'Мужской')]

class Category(models.Model):
    name  = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('main:product_list_by_category', args=[self.slug])
    def get_men_url(self):
        return reverse('main:product_list_men_by_category', args=[self.slug])
    def get_women_url(self):
        return reverse('main:product_list_women_by_category', args=[self.slug])
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',
                                 on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, default='Женский')
    size = models.IntegerField(max_length=10, default=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    discount = models.DecimalField(default=0.00, max_digits=5,
                                   decimal_places=2)
    

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['id', 'slug']),
                   models.Index(fields=['name']),
                   models.Index(fields=['-created'])]


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('main:product_detail', args=[self.slug])
    
    def get_formatted_price(self):
        if self.price == int(self.price):
            return int(self.price)
        return self.price
    
    def sell_price(self):
        if self.discount:
            self.price = round(self.price-self.price*self.discount/100, 2)
            return self.get_formatted_price()
        return self.price
    