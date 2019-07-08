# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
@python_2_unicode_compatible   # Python 2 support.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    """
    It’s important to add __str__() methods to your models, not only for your
    own convenience when dealing with the interactive prompt, but also because
    objects’ representations are used throughout Django’s
    automatically-generated admin.
    """
    def __str__(self):
        return self.question_text

    # Custom method.
    def was_published_recently(self):
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

        # Adding future date check.
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


@python_2_unicode_compatible   # Python 2 support.
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # Always add a __str__ method.
    def __str__(self):
        return self.choice_text
