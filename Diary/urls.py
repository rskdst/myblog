from django.urls import path,re_path
from Diary import views
urlpatterns = [
    re_path('^$',views.diary),
    re_path('(?P<article_id>\d+).html/',views.diary_content),
    path('studydiary/',views.studydiary),
    re_path('^studydiary/(?P<article_id>\d+).html/$',views.diary_content),
]