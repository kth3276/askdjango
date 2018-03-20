# accounts/models.py

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)  # 나중에 교정할것 원투원은 하나의 유저의 하나의 정보만 가능
    phone_number = models.CharField(max_length=20)
    adress = models.CharField(max_length=50)