from django.db import models

class Answer(models.Model):
    class Meta:
      db_table = 'answers'

    question = models.ForeignKey('questions.Question', on_delete=models.CASCADE)  
    content = models.TextField()
    name = models.CharField()
