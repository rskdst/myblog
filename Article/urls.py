from django.urls import path,re_path
from Article import views
urlpatterns = [
    re_path('^$',views.article),
    re_path('(?P<article_id>\d+).html/',views.article_content),
]