from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32)
    author = models.ForeignKey("Author",on_delete=models.CASCADE)
    article_id = models.CharField(max_length=10,unique=True)
    content = RichTextField()
    description = RichTextField()
    type = models.CharField(max_length=10,default="技术文章")
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField("Tag")

    def __str__(self):
        return "<oj:%s>"%self.title

class Author(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return "<obj:%s>"%self.name

class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return "<obj:%s>"%self.name

