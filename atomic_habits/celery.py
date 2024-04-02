from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'atomic_habits.settings')

app = Celery('atomic_habits')

app.config_from_object('django.conf:atomic_habits', namespace='CELERY')

app.autodiscover_tasks()
