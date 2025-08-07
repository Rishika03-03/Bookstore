from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json
import os

# 📚 Book data for homepage & cart
BOOKS = [
    {'id': 1, 'title': 'The Midnight Library', 'price': 499, 'image': 'https://m.media-amazon.com/images/I/81J6APjwxlL.jpg'},
    {'id': 2, 'title': 'Ikigai', 'price': 299, 'image': 'https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcTCSzxdswCKBDPvYef3odRrW7LIRziBPIT1jt294tcpSztK6t8cBwsCUmzEuN_mMoRcW-SuRtbCnLVDb79de3eTz5tP_oomIY79gWqkTMYseSqNX6ZW4jVK&usqp=CAc'},
    {'id': 3, 'title': 'Rich Dad Poor Dad', 'price': 399, 'image': 'https://m.media-amazon.com/images/I/81bsw6fnUiL._SL1500_.jpg'},
    {'id': 4, 'title': 'Deep Work', 'price': 429, 'image': 'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1447957962i/25744928.jpg'},
    {'id': 5, 'title': 'The Psychology of Money', 'price': 349, 'image': 'https://m.media-amazon.com/images/I/71g2ednj0JL._SL1500_.jpg'},
    {'id': 6, 'title': 'Atomic Habits', 'price': 450, 'image': 'https://m.media-amazon.com/images/I/91bYsX41DVL._SL1500_.jpg'},
]

def home(request):
    return render(request, 'store/home.html', {'books': BOOKS})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "store/login.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("register")

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Registration successful. Please log in.")
        return redirect("login")

    return render(request, "store/register.html")

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        messages.success(request, "Message sent successfully!")
        return redirect("contact")
    return render(request, "store/contact.html")

def category_view(request):
    if request.method == "POST":
        user_action = request.POST.get("action")
        if user_action:
            return render(request, "store/action.html")
    return render(request, "store/categories.html")

def action_view(request):
    return render(request, "store/action.html")

def comedy_view(request):
    return render(request, "store/comedy.html")

def fictional_view(request):
    return render(request, "store/fictional.html")

def horror_view(request):
    return render(request, "store/horror.html")

def motivational_view(request):
    return render(request, "store/motivational.html")

def thriller_view(request):
    return render(request, "store/thriller.html")

def cart_view(request):
    cart = request.session.get('cart', [])
    cart_items = [book for book in BOOKS if book['id'] in cart]
    total_price = sum(book['price'] for book in cart_items)
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, book_id):
    cart = request.session.get('cart', [])
    cart.append(book_id)
    request.session['cart'] = cart
    return redirect('home')

@login_required(login_url='/login/')
def buy_now(request):
    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        payment_method = request.POST.get("payment_method")

        order_data = {
            "username": request.user.username,
            "name": name,
            "address": address,
            "payment_method": payment_method
        }

        file_path = "orders.json"
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                existing_orders = json.load(f)
        else:
            existing_orders = []

        existing_orders.append(order_data)

        with open(file_path, "w") as f:
            json.dump(existing_orders, f, indent=2)

        messages.success(request, f"Order placed successfully via {payment_method}")
        return render(request, "store/confirmation.html", {
            "name": name,
            "address": address,
            "payment_method": payment_method
        })

    return render(request, "store/buynow.html")

def my_account(request):
    if not request.user.is_authenticated:
        return redirect('login')
    cart = request.session.get("cart", [])
    return render(request, "store/myaccount.html", {
        "cart": cart,
        "user": request.user
    })

def logout_view(request):
    logout(request)
    return redirect("home")


def my_orders(request):
    if not request.user.is_authenticated:
        return redirect('/login/')  # manually redirect if not logged in

    file_path = "orders.json"
    user_orders = []

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            all_orders = json.load(f)
            user_orders = [order for order in all_orders if order["username"] == request.user.username]

    return render(request, "store/my_orders.html", {"orders": user_orders})

def help_page(request):
    return render(request, 'store/help.html')



