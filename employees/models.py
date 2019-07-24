from django.db import models

# Create your models here.

class Employees(models.Model):
    employee = models.CharField(max_length=50)
