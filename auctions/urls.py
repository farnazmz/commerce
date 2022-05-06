from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listings", views.listings, name="listings"),

    path("categories", views.categories, name="categories"),
    path("category_page", views.category_page, name="category_page"),
 
    path("listings_view", views.listings_view, name="listings_view"),
    path("listings_view/<str:listing_id>", views.listings_view, name="listings_view"),

    path("watchlist/<str:listing_id>", views.watchlist, name="watchlist"),
    path("watchlist/<int:user_id>", views.watchlist, name="watchlist"),
    path("watchlist", views.watchlist, name="watchlist"),

    path("bid/<str:listing_id>", views.bid, name="bid"),
    path("bid", views.bid, name="bid"),  
   
]
   
      
      
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
 
