


from django.core.management import call_command

from django.contrib.auth.models import AbstractUser
from django.db import models
import email

from email.policy import default
from operator import mod
from sre_parse import CATEGORIES
from time import timezone
from tkinter import CASCADE
from typing import Any
from unicodedata import category
from click import password_option


from django.urls import reverse
from sqlalchemy import false

class User(AbstractUser):
    pass


class Listings(models.Model):
    CATEGORIES= [
    ('clothing, shoes', 'Clothing, Shoes'),
    ('jewelry, watches', 'Jewelry, Watches'),
    ('books', 'Books'),
    ('electronics', 'Electronices'),
    ('home, garden, tools', 'Home, Garden, Tools'),
    ('beauty, health', 'Beauty, Health'),
    ('outdoors', 'Outdoors'),
    ('handmade', 'Handmade'),
    ('toys, kids, baby', 'Toys, Kids, Baby'),
    ('pet supplies', 'Pet Supplies'),
    ('sports', 'Sports')
    ] 
    
    title = models.TextField(max_length=64)
    price = models.FloatField()
    description = models.CharField(max_length=1000)
    image = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    category = models.CharField(max_length=50, choices=CATEGORIES)
    active = models.BooleanField(default=True)

    def __str__(self):
            return f"{self.title} \n {self.category} \n {self.price} \n {self.creation_date} \n {self.image} \n {self.description}"

    def get_absolute_url(self): 
            return reverse('listings_view', args=[str(self.id)])


