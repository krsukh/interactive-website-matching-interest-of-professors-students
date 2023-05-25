from django.contrib import auth
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from userapp.models import User


def login_view(request):
    if request.method == "POST":
        print("hello")
        username = request.POST['username']
        password = request.POST['password']
        remember = request.POST.get("remember", "off")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print("login")
            if remember == "on":
                request.session['username'] = username
                request.session['password'] = password
                print("session created")
                print(request.user)
            return redirect('/dashboard/')
        # elif User.objects.filter(username=username).exists():
        #      print("username__found")
        #
        #      auth.login(request, user)
        #      print("login")
        #      if remember == "on":
        #          request.session['username'] = username
        #          request.session['password'] = password
        #          print("session created")
        #
        #      print(request.user)
        #      return redirect('/dashboard/')
        else:
            print("username_not_found")
            username_not_found = True



    else:
        username = request.session.get("username", "")
        password = request.session.get("password", "")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print(request.user)
            return redirect('/dashboard/')
        else:
           password_error = True

           print("not login")

    return render(request, "loginapp/login.html", locals())



@login_required(login_url="/")
def logout_view(request):
    del request.session['username']
    del request.session['password']
    logout(request)
    return  redirect("/")




