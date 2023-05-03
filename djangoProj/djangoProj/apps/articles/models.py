import datetime
from django.db import models
from django.utils import timezone


class Article(models.Model):
    a_title = models.CharField("name of the article", max_length = 200)
    a_content = models.TextField("articles text")
    a_pub_dt = models.DateTimeField('public date')

    def __str__(self):
        return self.a_title

    def was_pb_recently(self):
        return self.a_pub_dt >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    a_id = models.ForeignKey(Article, on_delete = models.CASCADE)
    c_au_name = models.CharField('name of an  author', max_length = 50)
    c_content = models.TextField('comments text')

    def __str__(self):
        return (f"{self.c_au_name} - {self.c_content}")

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'