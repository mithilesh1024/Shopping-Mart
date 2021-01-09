from django.urls import path,include
from . import views

urlpatterns = [
    path('buyersignup/', views.signup, name='costumerSignUp'),
    path('buyersignin/', views.signin, name='costumerSignIn'),
    path('cart/', views.cart, name='cart'),
    path('', views.index, name='index'),
]
