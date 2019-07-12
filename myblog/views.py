from django.shortcuts import render


def index(req):

    return render(req,"index.html")


def about(req):
    return render(req,"about.html")

def listpic(req):
    return render(req,"listpic.html")

def newslistpic(req):
    return render(req,"diary.html")
