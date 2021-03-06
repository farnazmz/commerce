
from random import expovariate
import django
from enum import auto
from pyexpat import model
import re
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
from requests import request, session
from sqlalchemy import false, true

class User(AbstractUser):
    pass


class Listing(models.Model):
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
    image = models.ImageField(upload_to='auctions\image')
    creation_date = models.DateTimeField(auto_now=True, blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listing")
    category = models.CharField(max_length=50, choices=CATEGORIES)
    active = models.BooleanField() 
<<<<<<< HEAD
    
=======
     
>>>>>>> 1fe2dc96e6236ac945d05bc8438c60297a24367c
    def __str__(self):
        return f"{self.id}"
    
    def get_absolute_url(self): 
        return reverse('listings_view', args=[str(self.id)])


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True)
    is_on_watchlist = models.CharField(max_length=64, null=True, blank=True, default="")

    def __str__(self):
        return f"{self.listing}"
<<<<<<< HEAD
        
  
=======


>>>>>>> 1fe2dc96e6236ac945d05bc8438c60297a24367c
class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE) 
    bid_time = models.DateTimeField(auto_now_add=True)
    bid_amount = models.FloatField(null=True)
  
    
class Comment(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)  
    comment = models.TextField(null=True) 
    time_sent = models.DateTimeField(null=True) 

    def __str__(self):
            return f"{self.comment}" 
   