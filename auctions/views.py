from asyncio.constants import LOG_THRESHOLD_FOR_CONNLOST_WRITES
from cProfile import label
from email import message
from multiprocessing import context
from multiprocessing.sharedctypes import Value
from sre_parse import CATEGORIES
from telnetlib import LOGOUT
from tkinter import Widget
from turtle import title
from unicodedata import category
from attr import attr
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, path
from django import forms
from django.db import models
from requests import request
from .models import User
from .models import Listings
from .forms import ListingsForm, CategoriesForm



from xml.dom.minidom import Attr
from tkinter.tix import Form
import datetime
from .forms import  CategoriesForm, ListingsForm
from auctions import forms
  
def index(request):  
    listings = Listings.objects.all()
    for listing in listings:
        return render(request, "auctions/index.html", {
                "listing": listing,
                "listings": listings
            })    


def login_view(request):
    if request.method == "POST":
    # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


login_required()
def listings(request):
    if request.method == "POST":
        form = ListingsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            category = form.cleaned_data["category"]
            price = form.cleaned_data["price"]
            description = form.cleaned_data["description"]
            image = form.cleaned_data["image"]
            acitve =  form.cleaned_data["active"]                  
            listing = Listings(
                seller=request.user,
                title=title,
                category=category,
                price=price,
                description=description,
                image=image, 
                active=acitve
            )
            listing.save()
            return redirect("index")
        else:
            return render(request, "auctions/listings.html", {
                "form": form,
                "message": "Invalid"
            })
    else:
        return render(request, "auctions/listings.html", {
            "form":ListingsForm()
        })

login_required()
def listings_view(request, listing_id):
    listings = Listings.objects.get(id=listing_id)
    
    return render(request, "auctions/listings_view.html", {
            "listings":listings,          
        })

login_required()
def categories(request):
    
    if request.method == "GET":
        return render(request, "auctions/categories.html", {                      
                "form":CategoriesForm(),
                  "a": "a"       
                })
    else:
        return render(request, "auctions/category_page.html")


login_required()
def category_page(request):
    form = CategoriesForm(request.POST)      
    if form.is_valid():
        category_name = form.cleaned_data["category"]
        listings = Listings.objects.filter(category=category_name)
     
        return render(request, "auctions/category_page.html", {
                    "listings":listings,                                   
                    "category_name":category_name,
                    "form":form                                   
            })
           
    else:        
        return render(request, "auctions/categories.html", {                      
                "form":CategoriesForm(),   
                "b":"b"  
                })     
 
    
