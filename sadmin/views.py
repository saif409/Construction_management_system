from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail


# Create your views here.


def testview(request):
    return HttpResponse(request, "this is test")


def user_login(request):
    if request.method == "POST":
        user = request.POST.get('user', )
        password = request.POST.get('pass', )
        auth = authenticate(request, username=user, password=password)
        if auth is not None:
            login(request, auth)
            return redirect('home')
        else:
            messages.add_message(request, messages.ERROR, 'Username or password mismatch!')
    return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect('login')


def home(request):
    context={
        "isact_home": "active"
    }
    return render(request, "admin_home.html", context)

