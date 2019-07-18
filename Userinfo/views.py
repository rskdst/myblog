from django.shortcuts import render,HttpResponse,redirect
from .form import *
from django.http import JsonResponse
from .models import UserInfo
import hashlib
# Create your views here.
def encrypt_password(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    return md5.hexdigest()


def register(req):
    print(req.method)
    if req.method == "GET":
        form = RegisterForm()
        return render(req,"register_login.html",locals())
    else:
        print(req.POST)
        form = RegisterForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            password = encrypt_password(password)
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
            if req.session.get("username"):
                req.session.flush()
                req.session["username"] = form.cleaned_data["username"]
            else:
                req.session["username"] = form.cleaned_data["username"]
            return redirect("/index/")
        else:
            if form.errors.get("username"):
                error = form.errors["username"][0]
            else:
                error = form.errors["password"][0]
            return render(req,"register_login.html",locals())


def logout(req):
    req.session.flush()
    print(req.session.get("username"))
    return redirect(req.META["HTTP_REFERER"])