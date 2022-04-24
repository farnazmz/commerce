from cProfile import label
from email.policy import default
from sre_parse import CATEGORIES
from typing import Any
from unicodedata import category
from django import forms
from .models import User, Listings

class ListingsForm(forms.Form):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={"PlaceHolder":"Title"}))

    image = forms.CharField(label="", widget=forms.TextInput(attrs={"PlaceHolder":"Image_URL"}))

    price = forms.FloatField(label="", widget=forms.NumberInput())

    description = forms.CharField(label="", widget=forms.TextInput(attrs={"PlaceHolder":"Description"}))  

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
    category = forms.CharField(label="", widget=forms.Select(choices=CATEGORIES))
    active = forms.BooleanField(required=False)


class CategoriesForm(forms.Form):
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
    category = forms.CharField(label="", widget=forms.Select(choices=CATEGORIES))
    active = forms.BooleanField(required=False)
    
   

 



