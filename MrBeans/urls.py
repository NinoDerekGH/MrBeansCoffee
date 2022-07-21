from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_out, name="home_out"),
    path('shop/', views.shop_out, name="shop_out"),
    path('faqs/', views.faqs_out, name="faqs_out"),
    path('about/', views.about_out, name="about_out"),
    path('contact/', views.contact_out, name="contact_out"),
    path('home_in/', views.home_in, name="home_in"),
    path('shop_in/', views.shop_in, name="shop_in"),
    path('faqs_in/', views.faqs_in, name="faqs_in"),
    path('about_in/', views.about_in, name="about_in"),
    path('contact_in/', views.contact_in, name="contact_in"),
    path('cart_in/', views.cart_in, name="cart_in"),
]