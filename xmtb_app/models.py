from django.db import models
from datetime import *
from django.contrib.auth import get_user_model

User = get_user_model()

class Products(models.Model):
    create_date = models.DateField(auto_now=True)
    heading = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    brand = models.ForeignKey('Brands', on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    city = models.ForeignKey('Cities', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    tel_number = models.CharField(max_length=13, blank=True, null=True)
    link = models.URLField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

 

    class Meta:
        verbose_name = 'Products'
        verbose_name_plural = 'Products'

class Brands(models.Model):
    brand = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return '{}'.format(self.brand)
    
    class Meta:
        verbose_name = 'Brands'
        verbose_name_plural = 'Brands'
    
class Categories(models.Model):
    category = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return '{}'.format(self.category)

    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'


class Cities(models.Model):
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return '{}'.format(self.name)
    
    class Meta:
        verbose_name = 'Cities'
        verbose_name_plural = 'Cities'