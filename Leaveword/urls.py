from django.urls import path,re_path
from Leaveword import views
urlpatterns = [
    re_path('^$',views.leaveword),
]