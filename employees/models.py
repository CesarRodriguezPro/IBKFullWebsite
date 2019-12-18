from django.db import models

class RecordView(models.Model):
    last_name = models.CharField(max_length=40)
    first_name = models.CharField(max_length=40)
    time = models.DateTimeField(auto_now=True)
