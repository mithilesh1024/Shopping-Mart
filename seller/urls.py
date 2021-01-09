from django.urls import path
from . import views


urlpatterns = [
    path('sellersigup/', views.sellersignup, name='sellerSignUp'),
    path('sellersigin/', views.sellersignin, name='sellerSignIn'),
    path('productdetails/', views.productDetail, name='productdetails'),
]
