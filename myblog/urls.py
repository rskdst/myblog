"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from myblog import views as mv
from Userinfo import views as uv
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',mv.about),
    path('index/', mv.index),
    path('listpic/',mv.listpic),
    re_path(r'^diary/',include("Diary.urls")),
    re_path(r'^article/',include("Article.urls")),
    path('search/', mv.search),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('login/', uv.login),
    path('register/', uv.register),
    re_path(r'^leaveword/',include("Leaveword.urls")),
    path('logout/', uv.logout),

]
