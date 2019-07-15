from django.db import models
# Create your models here.
class Diary(models.Model):
    title = models.CharField(max_length=100)
    diary_id = models.CharField(max_length=10)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "<obj:%s>"%self.title

class StudyDiary(models.Model):
    title = models.CharField(max_length=100)
    diary_id = models.CharField(max_length=10)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "<obj:%s>"%self.title
