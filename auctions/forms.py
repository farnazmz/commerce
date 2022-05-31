from cProfile import label
from email.policy import default
from hashlib import blake2b
from importlib.metadata import files
from pickle import TRUE
from random import choices
from select import select
from sre_parse import CATEGORIES
from tkinter import Widget
from tkinter.tix import Select
from typing import Any
from unicodedata import category
from attr import fields
from django import forms
from django.forms import BooleanField, ChoiceField, ModelForm, NullBooleanSelect
from sqlalchemy import true, false, null
from .models import Watchlist, Bid, Comment, User, Listing


class ListingForm(forms.Form):

    title = forms.CharField(label="", widget=forms.TextInput(attrs={"PlaceHolder":"Title"}))
    price = forms.FloatField(label="", widget=forms.NumberInput(attrs={"PlaceHolder":"Price"}))
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
    image = forms.ImageField(label="")
    active = forms.NullBooleanField(required=False, label="switch", widget=forms.Select(choices=[('true', 'Active'), ('false', 'Not Active')]))


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


class WatchlistForm(forms.Form):
    change_view = forms.NullBooleanField(required=False, label="", widget=forms.Select(choices=[('true', 'Add to Watchlist'), ('false', 'Remove from Watchlist')]))
    

class BidForm(forms.Form):
    bid_amount = forms.FloatField(label="", widget=forms.NumberInput(attrs={"PlaceHolder":"Bid"}), required=False)


class CommentForm(forms.Form):
    comment = forms.CharField(label="", widget=forms.TextInput(attrs={"PlaceHolder":"Comment"}), required=False)
    

class EditForm(forms.Form):
    active = forms.NullBooleanField(required=False, label="", widget=forms.Select(choices=[('true', 'Active'), ('false', 'Not Active')]))
