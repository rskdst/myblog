from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Diary(models.Model):
    title = models.CharField(max_length=100)
    article_id = models.CharField(max_length=10)
    content = RichTextField()
    description = RichTextField()
    type = models.CharField(max_length=10, default="个人日记")
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "<obj:%s>"%self.title

class StudyDiary(models.Model):
    title = models.CharField(max_length=100)
    article_id = models.CharField(max_length=10)
    content = RichTextField()
    description = RichTextField()
    type = models.CharField(max_length=10, default="学习笔记")
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "<obj:%s>"%self.title
