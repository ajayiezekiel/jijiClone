from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICES = (
    ('VEHICLES','vehicles'),
    ('PHONES', 'phones'),
    ('PROPERTY', 'property'),
    ('ELECTRONICS', 'electronics'),
    ('FASHION', 'fashion'),
)

class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    price = models.FloatField()
    location = models.CharField(max_length=250)
    imageUrl = models.URLField()
    isSold = models.BooleanField(default=False)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='models')
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='phones')
    createdAt = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Buyer(models.Model): 
    name = models.CharField(max_length=250)
    phoneNumber = models.CharField(max_length=250)
    emailAddress = models.EmailField(max_length=250)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name='models')

    def __str__(self):
        return self.name


