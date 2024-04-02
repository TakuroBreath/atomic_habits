from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=40, verbose_name='phone', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='country', **NULLABLE)
    telegram_id = models.PositiveIntegerField(default=None, verbose_name='telegram_id', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
