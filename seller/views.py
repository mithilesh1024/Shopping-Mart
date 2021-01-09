from django.shortcuts import render

# Create your views here.


def sellersignup(request):
    return render(request, 'seller/SellerSignUp.html')

def sellersignin(request):
    return render(request, 'seller/SellerSignIn.html')

def productDetail(request):
    return render(request, 'seller/ProductDetails.html')
