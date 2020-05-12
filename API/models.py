from django.db import models
from django.contrib.auth.models import User


class Interview(models.Model):
    name = models.CharField(max_length = 150, primary_key = True)
    description = models.CharField(max_length = 1000)
    start_date = models.DateTimeField(auto_now_add = True)
    end_date = models.DateTimeField(null = True, blank = True)
    active = models.BooleanField(default = True)
    def __str__(self):
        return ''.join([self.name,])

class Question(models.Model):
    TEXT, ONE_OPTION, MANY_OPTIONS = 'Text', 'One Option', 'Many Options'
    TYPE_CHOICES = (
        (TEXT, 'Text'),
        (ONE_OPTION, 'One Option'),
        (MANY_OPTIONS, 'Many Options')
    )
    id = models.AutoField(primary_key = True)
    interview = models.ForeignKey(Interview, on_delete = models.CASCADE)
    text = models.CharField(max_length = 1000)
    type = models.CharField(choices = TYPE_CHOICES, max_length = 20, default = TEXT)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
    text = models.CharField(max_length = 500)
    id = models.AutoField(primary_key = True)
