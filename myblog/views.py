from django.shortcuts import render
from django.http import HttpResponse
from Article.models import *
from Diary.models import *

def index(req):
    diary = Diary.objects.order_by("-update_date").values("title","description","article_id","update_date").first()
    study_diary = StudyDiary.objects.order_by("-update_date").values("title","description","article_id","update_date")[:2]
    article = Article.objects.order_by("-update_date").values("article_id","title","description","update_date","author__name")[:3]
    return render(req,"index.html",locals())


def about(req):
    return render(req,"about.html")

def listpic(req):
    return render(req,"listpic.html")

def newslistpic(req):
    return render(req,"diary.html")

def search(req):
    data_list = []
    keyword = req.GET.get("keyboard")
    diary = Diary.objects.filter(title__contains=keyword).order_by("-update_date").values("title","description","article_id","update_date")
    study_diary = StudyDiary.objects.filter(title__contains=keyword).order_by("-update_date").values("title","description","article_id","update_date")
    article = Article.objects.filter(title__contains=keyword).order_by("-update_date").values("article_id","title","description","update_date","author__name")
    for d in diary:
        if d:
            data_list.append(d)
        else:
            pass
    for s in study_diary:
        if s:
            data_list.append(s)
        else:
            pass
    for a in article:
        if a:
            data_list.append(a)
        else:
            pass
    # print(data_list)
    return render(req,"search.html",{"data_list":data_list})

