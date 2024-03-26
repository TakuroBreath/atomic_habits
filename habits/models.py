from django.contrib.auth import get_user_model
from django.db import models

from users.models import NULLABLE


class Award(models.Model):
    name = models.TextField()


class Habit(models.Model):
    user = models.ForeignKey(get_user_model(), verbose_name='user')
    place = models.CharField(max_length=100, verbose_name='place')
    time = models.DateTimeField(verbose_name="time to do")
    action = models.TextField(verbose_name='action')
    is_pleasant = models.BooleanField(verbose_name='is pleasant')
    parent_habit = models.ForeignKey('self', verbose_name='parent habit', on_delete=models.SET_NULL, **NULLABLE)
    periodic = models.PositiveSmallIntegerField(verbose_name='periodic', default=1)
    award = models.ForeignKey(Award, verbose_name='award', on_delete=models.CASCADE)
    time_for_action = models.DateTimeField(verbose_name='time for action')
    is_public = models.BooleanField(verbose_name='is public')
