from django.contrib import admin
from .models import Auction, User, Listing, Bid, Comment, Watchlist

# Register your models here.
admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Auction)
admin.site.register(Watchlist)
admin.site.register(Bid)
admin.site.register(Comment)




    
