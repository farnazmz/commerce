from cProfile import label
from email.policy import default
from random import choices
from select import select
from sre_parse import CATEGORIES
from tkinter.tix import Select
from typing import Any

from unicodedata import category
from django import forms


class ListingForm(forms.Form):

    title = forms.CharField(label="", widget=forms.TextInput(attrs={"PlaceHolder":"Title"}))
    image = forms.ImageField(max_length=200)
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


class CategoryForm(forms.Form):
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

class WatchlistForm(forms.Form):
    
   
    change_watch = forms.BooleanField (required=False, widget=forms.Select(choices=[
        ('true', 'Add to Watchlist'),
        ('false', 'Remove from Watchlist')
    ]))


class BidForm(forms.Form):
    bid_amount = forms.FloatField(label="", widget=forms.NumberInput(), required=False)


class CommentForm(forms.Form):
    comment = forms.CharField(label="", widget=forms.TextInput(attrs={"PlaceHolder":"Comment"}), required=False)
    

