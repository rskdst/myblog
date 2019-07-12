from django.shortcuts import render
from Article import models
from django.core.paginator import Paginator,Page
# Create your views here.
def article(req):
    content_lst = []
    current_page = int(req.GET.get("page", 1))
    start_content = (current_page - 1) * 6
    stop_content = current_page * 6
    all_data = models.Article.objects.all()
    data = models.Article.objects.all()[start_content:stop_content]
    paginator = Paginator(all_data, 6)
    num_pages = paginator.num_pages
    page = paginator.page(current_page)
    for i in data:
        print(i.content)
        content_lst.append(i.content[0:30])
    return render(
        req,
        "article.html",
        {
            "data": data,
            "num_pages": num_pages,
            "page": page,
            "content_list": content_lst,
        }
    )
    


def article_content(req,article_id):
    data = models.Article.objects.filter(article_id=article_id).values("title","author__name","content","created_date")[0]
    print(data)
    return render(
        req,
        "article_content.html",
        {
            "data":data
        }
    )