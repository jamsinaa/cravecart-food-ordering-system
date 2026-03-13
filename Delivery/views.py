from django.shortcuts import render, redirect
from .models import Menu
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Restaurant
from .models import Restaurant, Menu, Order
from django.contrib.auth.forms import UserCreationForm



def index(request):
    restaurants = Restaurant.objects.all()

    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())

    return render(request, "Delivery/index.html", {
        "restaurants": restaurants,
        "cart_count": cart_count
    })


def signin(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "Delivery/signin.html")

    return render(request, "Delivery/signin.html")


def signup(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        User.objects.create_user(username=username, password=password)

        return redirect("/signin")

    return render(request, "Delivery/signup.html")


def signout(request):
    logout(request)
    return redirect("/")

def restaurant_menu(request, id):
    restaurant = Restaurant.objects.get(id=id)
    menus = Menu.objects.filter(restaurant=restaurant)

    return render(request, "Delivery/menu.html", {
        "restaurant": restaurant,
        "menus": menus
    })

def add_to_cart(request, item_id):
    cart = request.session.get('cart', {})

    if isinstance(cart, list):
        cart = {}

    item_id = str(item_id)

    if item_id in cart:
        cart[item_id] += 1
    else:
        cart[item_id] = 1

    request.session['cart'] = cart

    return redirect('/cart/')


def cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for item_id, quantity in cart.items():
        menu_item = Menu.objects.get(id=item_id)
        menu_item.quantity = quantity
        cart_items.append(menu_item)

        total += menu_item.price * quantity

    return render(request, "Delivery/cart.html", {
        "cart_items": cart_items,
        "total": total
    })

def remove_from_cart(request, index):
    cart = request.session.get('cart', [])

    if index < len(cart):
        cart.pop(index)

    request.session['cart'] = cart
    return redirect('/cart/')

def increase_quantity(request, item_id):
    cart = request.session.get('cart', {})
    item_id = str(item_id)

    if item_id in cart:
        cart[item_id] += 1

    request.session['cart'] = cart
    return redirect('/cart/')


def decrease_quantity(request, item_id):
    cart = request.session.get('cart', {})
    item_id = str(item_id)

    if item_id in cart:
        cart[item_id] -= 1

        if cart[item_id] <= 0:
            del cart[item_id]

    request.session['cart'] = cart
    return redirect('/cart/')

def checkout(request):
    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        address = request.POST["address"]

        cart = request.session.get('cart', {})

        print("Order placed:", name, phone, address, cart)

        request.session['cart'] = {}

        return redirect('/order-success/')

    return render(request, "Delivery/checkout.html")

def order_success(request):
    return render(request, "Delivery/order_success.html")

def my_orders(request):
    orders = Order.objects.all().order_by('-created_at')

    return render(request,"Delivery/my_orders.html",{
        "orders":orders
    })