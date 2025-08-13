from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    return render(request, "index.html")

def login_page(request):
    return render(request, "login.html")

def register_page(request):
    return render(request, "register.html")

# Login View
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if not user.is_active:
                messages.error(request, "Your account is inactive. Please contact the admin.")
                return redirect('login_page')

            login(request, user)

            if user.is_staff or user.is_superuser:
                return redirect('adminhome')  # Make sure 'adminhome' URL name exists
            else:
                return redirect('userhome')   # Make sure 'userhome' URL name exists
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login_page')

    return render(request, 'login.html')

# Registration View
def user_registration(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        # Validation
        if not all([username, email, password, confirm_password, first_name, last_name]):
            messages.error(request, "All fields are required.")
            return redirect('register_page')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register_page')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register_page')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('register_page')

        # Create inactive user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_active = False
        user.save()

        messages.success(request, "Registration successful! Wait for admin approval.")
        return redirect('login_page')

    return render(request, 'register.html')

# Logout View
def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login_page')
