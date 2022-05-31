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
    path("watchlist", views.watchlist, name="watchlist"),
    path("<int:listing_id>", views.watchlist_change, name="watchlist_change"),
    path("bid", views.bid, name="bid"), 
    path("bid/<int:listing_id>", views.bid, name="bid"), 
    path("comment", views.comment, name="comment"), 
    path("comment/<int:listing_id>", views.comment, name="comment"), 
    path("edit", views.edit, name="edit"), 
    path("edit/<int:listing_id>", views.edit, name="edit"),      
]
     
      
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
 
