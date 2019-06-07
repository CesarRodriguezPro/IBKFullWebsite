from django.db import models
from django.contrib.auth.models import AbstractUser


class UserMain(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)

