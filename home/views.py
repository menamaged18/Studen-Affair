from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from authenticationapp.views import custom_login_required


# @custom_login_required
# @login_required(login_url="user_login")  # Protect mainpage
@custom_login_required
def mainpage(request):
    return render(request, "home/mainpage.html")  # Load mainpage only for logged-in users

def user_logout(request):
    logout(request)
    return redirect("user_login")  # Redirect to login page after logout


@custom_login_required
def tutorialpage(request):
    return render(request, 'home/MyTutorialPage.html')
