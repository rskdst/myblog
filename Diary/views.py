from django.shortcuts import render,HttpResponse
from Diary import models
from django.core.paginator import Paginator,Page
# Create your views here.
def diary(req):
    current_page = int(req.GET.get("page",1))
    start_content = (current_page-1)*6
    stop_content = current_page*6
    all_data = models.Diary.objects.order_by("-update_date")
    data = all_data[start_content:stop_content]
    paginator = Paginator(all_data,6)
    num_pages = paginator.num_pages
    page = paginator.page(current_page)
    return render(
        req,
        "diary.html",
        {
            "data":data,
            "num_pages":num_pages,
            "page":page,
            "req":req
        }
    )
def diary_content(req,article_id):
    if article_id.startswith("3"):
        data = models.StudyDiary.objects.filter(article_id=article_id).values("title","content","created_date")[0]
    else:
        data = models.Diary.objects.filter(article_id=article_id).values("title", "content", "created_date")[0]
    return render(req,"diary_content.html",{"data":data,"req":req})

def studydiary(req):
    current_page = int(req.GET.get("page", 1))
    start_content = (current_page - 1) * 6
    stop_content = current_page * 6
    all_data = models.StudyDiary.objects.order_by("-update_date")
    data = all_data[start_content:stop_content]
    paginator = Paginator(all_data, 6)
    num_pages = paginator.num_pages
    page = paginator.page(current_page)
    return render(
        req,
        "study_diary.html",
        {
            "data": data,
            "num_pages": num_pages,
            "page": page,
            "req":req
        }
    )
