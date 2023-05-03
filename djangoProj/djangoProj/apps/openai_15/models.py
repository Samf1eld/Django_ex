import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    q_name = models.CharField("name of the question", max_length = 200)
    q_request = models.TextField("question request text")
    q_response = models.TextField("question response(answer) text", null=True)
    q_date_req = models.DateTimeField('request date')
    q_date_res = models.DateTimeField('response date', null=True)

    def __str__(self):
        return self.q_name

    def was_asked_recently(self):
        return self.q_date_req >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Question to AI'
        verbose_name_plural = 'Questions to AI'