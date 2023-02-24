from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.

def user_login(request):

    """This method will be used to authenticate direct user to login page

    :returns: directs user to authentication/login.html
    """

    return render(request, 'authentication/login.html')

def authenticate_user(request):

    """This method will be used to authenticate user password and username credentials

    :param str username: The user's username
    :param str password: The user's password

    :returns: Correct input of the two variables redirects to page confirming user is logged in
    """

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('user_auth:show_user')
        )



def show_user(request):

    """This method will be used to show user credentials

    :returns: renders user username and encrypted password    
    """

    print(request.user.username)
    return render(request, 'authentication/user.html', {
        'username': request.user.username,
        'password': request.user.password
    })

def register(response):

    """This method will be used to register new users

    :returns: directs new users to /vote/ page of website
    """

    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect('http://127.0.0.1:8000/vote/')
    else:
        form = RegisterForm()

    return render(response, 'authentication/register.html', {'form':form})
