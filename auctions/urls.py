from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listings", views.listings, name="listings"),

    path("listings_view", views.listings_view, name="listings_view"),
    path("listings_view/<int:listing_id>", views.listings_view, name="listings_view"),

    path("categories", views.categories, name="categories"),
    path("category_page", views.category_page, name="category_page"),
]
   
      
      
    
