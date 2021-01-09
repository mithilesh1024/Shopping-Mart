from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Cart, Costumer
from seller.models import Product
from buyer.utils import cal_price, add_to_cart, delete_cart_item, add_user, get_Products
from PIL import Image


# Create your views here.

def index(request):
    product = get_Products(Product.objects.all())
    data = {
        "prod": product
    }
    if request.method == "POST":
        print(request.POST)
        if request.POST.get("sign-out"):
            if "name" in request.session:
                del request.session["name"]
                del request.session["costumerID"]
                return redirect("index")
        if "name" in request.session:
            # print("name")
            if "add-to-cart" in request.POST:
                print("cant add")
                add_to_cart(int(request.POST.get("add-to-cart")), int(request.session.get("costumerID")))
    if "name" in request.session:
        data = {
            "prod": product,
            "name": request.session.get("name")
        }
        return render(request, "home.html", data)
    return render(request, "home.html", data)


def cart(request):
    data = {
        "user": request.session.get("name")
    }
    if "name" in request.session:
        if request.method == "POST":
            delete_cart_item(request.POST.get("remove-from-cart"))
        data = {
            "data": Cart.objects.filter(buyer=request.session.get("costumerID")),
            "price": cal_price(Cart.objects.filter(buyer=request.session.get("costumerID"))),
            "user": request.session.get("name")
        }
        # print(data)
        return render(request, "buyer/Cart.html", data)
    return render(request, "buyer/Cart.html", data)


def signup(request):
    if request.method == "POST":
        add_user(request.POST)
        return redirect("index")
    return render(request, "buyer/CustomerSignUp.html")


def signin(request):
    if "name" in request.session:
        return redirect("index")
    if request.method == "POST":
        print("post")
        if request.POST.get("login"):
            email = request.POST.get("email")
            password = request.POST.get("password")
            exist = Costumer.objects.filter(email=email, password=password).exists()
            print(f"${email} ${password} ${exist}")
            if exist:
                l = Costumer.objects.get(email=email, password=password)
                request.session["costumerID"] = l.id
                request.session["name"] = l.firstName
                return redirect("index")
            else:
                print("login error")
                mess = {
                    "error": "Email Or Password Is Wrong. Please try again."
                }
                # messages.error(request, "Email Or Password Is Wrong. Please try again.")
                return render(request, "buyer/CustomerSignIn.html", mess)
    return render(request, "buyer/CustomerSignIn.html")
