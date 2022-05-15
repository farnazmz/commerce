from mailbox import Message
from pyexpat.errors import messages
from typing import Any
from django import *
from ast import arg
from asyncio.constants import LOG_THRESHOLD_FOR_CONNLOST_WRITES
from cProfile import label
from email import message
from multiprocessing import context
from multiprocessing.sharedctypes import Value
from sre_parse import CATEGORIES
from telnetlib import LOGOUT
from tkinter import Widget
from attr import attr
from turtle import title
from unicodedata import category, name
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.forms import NullBooleanField
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, path
from sqlalchemy import false, null, true
from requests import request, session
from xml.dom.minidom import Attr
from tkinter.tix import Form
import datetime
from xml.etree.ElementTree import Comment
from tokenize import cookie_re
from .forms import WatchlistForm, BidForm, CommentForm, ListingForm, CategoryForm
from .models import User, Listing, Watchlist, Bid, Comment
from django.template import loader
from django.contrib import messages
from django.template import Context, Template

def index(request):  
    listings = Listing.objects.all()
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
def categories(request):   
    if request.method == "GET":
        return render(request, "auctions/categories.html", {                      
                "form":CategoryForm(),     
                })
    else:
        return render(request, "auctions/category_page.html")

login_required()
def category_page(request):
    form = CategoryForm(request.POST)      
    if form.is_valid():
        category_name = form.cleaned_data["category"]
        listings = Listing.objects.filter(category=category_name)    
        return render(request, "auctions/category_page.html", {
                    "listings":listings,                                   
                    "category_name":category_name,
                    "form":form                                   
            })          
    else:        
        return render(request, "auctions/categories.html", {                      
                "form":CategoryForm(),   
                "bid_form":BidForm()  
                })     

login_required()
def listings(request):
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data["title"]
            category = form.cleaned_data["category"]
            price = form.cleaned_data["price"]
            description = form.cleaned_data["description"]
            image = form.cleaned_data["image"]
            acitve =  form.cleaned_data["active"]                  
            listing = Listing(
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
            "form":ListingForm()
        })


login_required()
def watchlist_change(request, listing_id): 
    if request.method == "POST":
        watchlist_form = WatchlistForm(request.POST)
        if watchlist_form.is_valid():
            change_view =  watchlist_form.cleaned_data["change_view"]
            listing_id = Listing.objects.get(id=listing_id)
            watchlistitems = Watchlist.objects.filter(user=request.user, listing=listing_id)
            if watchlistitems:
                if not change_view:
                    Watchlist.objects.filter(user=request.user, listing=listing_id).delete()
                else:
                    messages.warning(request, 'Already on watchlist')
            else:
                if change_view:
                    w = Watchlist(user=request.user, listing=listing_id)
                    w.save()
                else:
                    messages.warning(request, 'Nothing to Remove!')

            return HttpResponseRedirect(reverse("watchlist"))
        else:
            messages.warning(request, 'Invalid Form')
    else:
        return HttpResponseRedirect(reverse("watchlist"))

login_required()
def watchlist(request):
    listing_id = Listing.objects.all()
    return render(request, "auctions/watchlist.html", {  
            "user":request.user,   
            "watchlists": Watchlist.objects.filter(user=request.user),
            "listing_id":listing_id,                                        
                })

login_required()
def bid(request, listing_id):
    if request.method == "POST":
        listing_id = Listing.objects.get(id=listing_id)
        h_price = listing_id.price
        h_price = float(h_price)
        bid_form = BidForm(request.POST)
        if bid_form.is_valid():
            bid_amount = bid_form.cleaned_data["bid_amount"]
            bid_amount = float(bid_amount)           
            if bid_amount > h_price:
                    b = Bid(
                        listing = listing_id,
                        bid_amount = bid_amount
                    )
                    b.save()
            else:
                messages.warning(request, 'make a higher bid')
                return HttpResponseRedirect(reverse("listings_view", kwargs={"listing_id":listing_id}))

            return HttpResponseRedirect(reverse("listings_view", kwargs={"listing_id":listing_id}))                          
        else:
            return HttpResponseRedirect(reverse("listings_view", kwargs={"listing_id":listing_id}))
    else:
        return HttpResponseRedirect(reverse("listings_view", kwargs={"listing_id":listing_id}))


login_required()
def comment(request, listing_id):
    if request.method == "POST":
        listing_id = Listing.objects.get(id=listing_id)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.cleaned_data["comment"]
            c = Comment(
                comment=comment,
                user=request.user,
                listing=listing_id
            )
            c.save()
            return HttpResponseRedirect(reverse("listings_view", kwargs={"listing_id":listing_id}))
        else:
            return HttpResponseRedirect(reverse("listings_view", kwargs={"listing_id":listing_id}))
    else:
        return HttpResponseRedirect(reverse("listings_view", kwargs={"listing_id":listing_id}))



      
login_required()
def listings_view(request, listing_id):  
    listing_id = Listing.objects.get(pk=listing_id)  
    bids = Bid.objects.filter(listing=listing_id)
    comments = Comment.objects.filter(listing_id=listing_id)
    watchin = Watchlist.objects.filter(listing=listing_id)
    watchers = [wa.user for wa in watchin]
    if not watchers:
        messages.warning(request, 'Be the first to watch.')    
    if bids:
        bid = [b.bid_amount for b in bids]
        bid_amount = max(bid)
    else:
        bid_amount = ""        
    if comments:
        comment = [c.comment for c in comments] 
        comment = str(comment)
    else:
        comment = str("")
    if request.user.is_authenticated:  
        return render(request, "auctions/listings_view.html", {
                            "comment_form":CommentForm(),
                            "bid_form":BidForm(),
                            "watchlist_form":WatchlistForm(),                   
                            "listing_id": listing_id,
                            "logged_in":request.user.is_authenticated,
                            "seller":str(request.user) == str(listing_id.seller),
                            "in_watchlist":Watchlist.objects.filter(user=request.user, listing=listing_id),
                            "is_authenticated":request.user.is_authenticated,
                            "listing":listing_id,
                            "bids":bids,
                            "bid_amount":bid_amount,
                            "comments":Comment.objects.filter(user=request.user, listing=listing_id),
                            "comment":comment,
                            "watchers":watchers,
                            
                            
                            
                            

                }) 
    else:            
        return render(request,"auctions/listings_view.html", { 
                "is_authenticated":request.user.is_authenticated,
                "listing":listing_id,
                "in_wachlist":false
                }) 
    