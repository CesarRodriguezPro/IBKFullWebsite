from django.db import models


class Drawings(models.Model):
    code_Id          = models.CharField(max_length=100)
    location         = models.CharField(max_length=100)
    drawings_no      = models.CharField(max_length=100)
    description      = models.CharField(max_length=100)
    date_submitted   = models.DateField()
