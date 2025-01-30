from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie

def no_cache_view(request):
    # Ensuring that the page is not cached, which is important for login pages
    response = render(request, 'pages/login.html')
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

def custom_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        # Debug: Print user authentication status
        print(f"User authenticated: {request.user.is_authenticated}")

        if not request.user.is_authenticated:
            messages.warning(request, "You need to sign in first.")
            return redirect('user_login')  # Redirect to login page
        return view_func(request, *args, **kwargs)

    return wrapper


def registerbtn(request):
    if request.method == 'POST':
        return redirect('register')
    return render(request, 'pages/register.html')

def register(request):
    if request.method == 'POST':
        logout(request)  # Force logout to clear previous session
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # Validate passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')
        
        # Create user
        try:
            user = User.objects.create_user(email=email, name=name, password=password)
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('user_login')  # Redirect to login page after successful registration
        except ValidationError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, "An error occurred during registration.")

    return render(request, 'pages/register.html')

@ensure_csrf_cookie
def user_login(request):
    logout(request)  # Ensure any logged-in user is logged out before showing the login page
    
    # i was using this to refresh the page every time we load the page but it has a problem so i did it using js 
    # if request.method == "POST":
    #     # On GET request, refresh CSRF token and render login page
    #     csrf_token = get_token(request)
    #     return render(request, 'pages/login.html', {"csrf_token": csrf_token})

    if request.method == "POST":
        email = request.POST.get("Email")
        password = request.POST.get("Password")
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("mainpage")  # Redirect to mainpage after login
        else:
            messages.error(request, "Invalid email or password.")  # Display error message

    return render(request, 'pages/login.html')  # Show login page
