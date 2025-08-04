from django.shortcuts import render, redirect


from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
import re

from django.contrib.auth import logout


from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, CartItem
from django.contrib.auth.decorators import login_required



def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})



@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        order = Order.objects.create(user=request.user, total_price=total)
        for item in cart_items:
            order.products.add(item)
        order.save()
        # Clear cart
        cart_items.delete()
        return redirect('order_success')

    return render(request, 'checkout.html', {'cart_items': cart_items, 'total': total})

@login_required
def order_success(request):
    return render(request, 'order_success.html')


def home(request):
    products = Product.objects.all()
    return render(request,'home.html', {'products':products})




def about(request):
    return render(request,'about.html')

def login_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Check if a user with the provided username exists
        if not User.objects.filter(email=email).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        # Authenticate the user with the provided username and password
        user = authenticate(email=email, password=password)
        
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('/home/')
    
    # Render the login page template (GET request)
    return render(request, 'login.html')

# Define a view function for the registration page
def register_view(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Password validation
        if (not re.search(r'[A-Z]', password) or
            not re.search(r'[a-z]', password) or
            not re.search(r'[0-9]', password) or
            not re.search(r'[^A-Za-z0-9]', password)):
            messages.error(request, "Password must include uppercase, lowercase, digit, and special character.")
            return redirect('register')

        # Name validation
        if not firstname.isalpha() or not lastname.isalpha() or not email.isalpha():
            messages.error(request, 'Names must contain only letters.')
            return redirect('register')


        # Save user securely
        User.objects.create_user(
            email=email,
            password=password,
            first_name=firstname,
            last_name=lastname
        )

        messages.success(request, 'Registration successful!')
        return redirect('login')

    # For GET request, render the registration form
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login_page')