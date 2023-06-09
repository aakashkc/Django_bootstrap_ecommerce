from django.db import models
from django.db.models.deletion import CASCADE
from category.models import Category
from django.urls import reverse
from  accounts.models import Account

# Create your models here.

class Product(models.Model):
    product_name=models.CharField(max_length=200, unique=True)
    slug=models.SlugField(max_length=200, unique=True)
    description=models.TextField(max_length=500, blank=True)
    price=models.IntegerField()
    images=models.ImageField(upload_to='static/images/products')
    stocks=models.IntegerField()
    is_available=models.BooleanField(default=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE) 
    #here what happens is whenever we delete a category it will deletes the product related to respective category.
    created_date=models.DateTimeField(auto_now_add=True)
    modefied_date=models.DateTimeField(auto_now=True)
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])


    def __str__(self):
        return self.product_name

class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager,self).filter(variation_category='color', is_active=True)


    def sizes(self):
        return super(VariationManager,self).filter(variation_category='size', is_active=True)
    
variation_category_choice = (
    ('color', 'color'),
    ('size', 'size'),

)

class Variation(models.Model):
    product                    =  models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category   =  models.CharField(max_length=100, choices=variation_category_choice)
    variation_value         =  models.CharField(max_length=100)
    is_active                   =   models.BooleanField(default=True)
    created_date            =   models.DateField(auto_now=True)

    objects=VariationManager()


    def __str__(self):
        return self.variation_value
    
#can also write
    # def __str__(self):
        # return self.variation_value

class ReviewRating(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    user=models.ForeignKey(Account, on_delete=models.CASCADE)
    subject=models.CharField(max_length=255, blank=True)
    review=models.TextField(max_length=500, blank=True)
    rating=models.FloatField()
    ip=models.CharField(max_length=20, blank=True)
    status=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.subject    
    