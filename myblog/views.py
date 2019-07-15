from django.shortcuts import render
from Article.models import *
from Diary.models import *

def index(req):
    diary = Diary.objects.order_by("-update_date").values("title","content","diary_id","update_date").first()
    diary_content = diary["content"][:30]
    study_diary = StudyDiary.objects.order_by("-update_date").values("title","content","diary_id","update_date")[:2]
    study_diary_content1 = study_diary[0]["content"][:30]
    study_diary_content2 = study_diary[1]["content"][:30]
    article = Article.objects.order_by("-update_date").values("article_id","title","content","update_date","author__name")[:3]
    article_content1 = article[0]["content"][:30]
    article_content2 = article[1]["content"][:30]
    article_content3 = article[2]["content"][:30]
    return render(req,"index.html",locals())


def about(req):
    return render(req,"about.html")

def listpic(req):
    return render(req,"listpic.html")

def newslistpic(req):
    return render(req,"diary.html")
