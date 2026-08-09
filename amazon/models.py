from django.db import models
from django.utils import timezone

# Create your models here.
#This is custom manager. 
class ProductManager(models.Manager):
    def available(self):
        return self.filter(
            is_active=True,
            stock__gt=0
        )


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.IntegerField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True,blank=True)

    objects = ProductManager() #custom manager object ...
    #after creating this object, now you can write Product.objects.available() --> this is is faster and more efficient than writing 
    """
    Product.objects.filter(
    is_active=True,
    stock__gt=0
    )
    """
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Order (models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )
    total = models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.name

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    quality = models.IntegerField()

    def __str__(self):
        return self.name

