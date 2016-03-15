# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=1000)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(blank=True, default=0)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name='qa_question_likes')

    def __str__(self):
        return self.title

    class Meta(object):
        ordering = ['-added_at']


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.text[:150]
