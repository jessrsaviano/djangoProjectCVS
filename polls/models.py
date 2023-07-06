
import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone

# Create your models here.
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')




