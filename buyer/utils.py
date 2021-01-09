from buyer.models import Costumer, Cart
from seller.models import Product
import base64


def cal_price(p):
    price = 0
    for temp in p:
        price = temp.products.price + price
    return price


def add_to_cart(productID, buyerID):
    # ** <QueryDict: {'csrfmiddlewaretoken': ['FQGDlqJotjvTSkoDTGuInzdEGx6kJjRUBfPCCZU8f5GNq9tpu12daCTdCEeu3XEH'], 'add_to_cart': ['Product object (2)']}>
    p = Product.objects.get(id=productID)
    b = Costumer.objects.get(id=buyerID)
    c = Cart(buyer=b, products=p)
    c.save()


def delete_cart_item(id):
    # ** <QueryDict: {'csrfmiddlewaretoken': ['dNYJHhfQxKhwBeCDvgmYdZsM8aZCwejh9c7IYQqAjwsq93Hp6BUt028l4h7MQS64'], 'remove-from-cart': ['2']}>
    Cart.objects.filter(products=id).first().delete()


def add_user(r):
    # ** <QueryDict: {'csrfmiddlewaretoken': ['q4JJgvFv8Lhhdhpx3QHYeCie8azKa5usmtSIx4QfUxsbL6ujEbft1FYN4hHUuJhf'], 'firstName': ['asdas'], 'lastName': ['asdasd'],
    # ** 'email': ['mithileshkapadi08@gmail.com'], 'address': ['h.no.920 vaishnav'], 'password': ['sadas'], 'sign-up': ['sign-up']}>
    firstname = r.get('firstName')
    lastName = r.get('lastName')
    email = r.get('email')
    address = r.get('address')
    password = r.get('password')
    c = Costumer(firstName=firstname, lastName=lastName, email=email, address=address, password=password)
    c.save()


def get_Products(products):
    for p in products:
        try:
            data = base64.b64encode(p.image)
            data = data.decode("UTF-8")
            p.image = data
        except:
            print("error")
    return products


def Cart_image(cart):
    for c in cart:
        try:
            data = base64.b64encode(c.products.image)
            data = data.decode("UTF-8")
            c.products.image = data
        except:
            print(f"error")
    return cart
