"""Import required libraries"""
import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin


class Question(models.Model):
    """Database table for Questions."""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )

    def __str__(self):
        """Function to assist with printing"""
        return str(self.question_text)

    def was_published_recently(self):
        """Corrected function that returns bool for recent questions"""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    """Database table for Question choices."""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.choice_text)
