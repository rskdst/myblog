from django.shortcuts import render,HttpResponse,redirect
from .form import *
from .models import UserInfo
# Create your views here.


def register(req):
    if req.method == "GET":
        form = RegisterForm()
        return render(req,"register_login.html",locals())
    else:
        form = RegisterForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            gender = form.cleaned_data["gender"]
            answer = form.cleaned_data["answer"]
            UserInfo.objects.create(username=username,password=password,gender=gender,answer=answer)
            return redirect("/login/")
        else:
            pass
        return render(req,"register_login.html",locals())


def login(req):
    url = "/login/"
    if req.method == "GET":
        form = LoginForm()
        return render(req,"register_login.html",locals())
    else:
        form = LoginForm(req.POST)
        if form.is_valid():
            return redirect("/index/")
        else:
            if form.errors.get("username"):
                error = form.errors["username"][0]
            else:
                error = form.errors["password"][0]
            return render(req,"register_login.html",locals())
