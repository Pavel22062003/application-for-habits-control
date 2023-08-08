from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='почта', unique=True)
    tg_chat_id = models.IntegerField(verbose_name='chat_id телеграм', **NULLABLE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
