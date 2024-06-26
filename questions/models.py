from django.db import models
from django.conf import settings


class Question(models.Model):
  class Meta:
    db_table = 'questions'

  title = models.CharField()
  content = models.TextField()
  name = models.CharField()
