from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class absentRequest(models.Model):
    foreman          = models.CharField(max_length=100,null=True, blank=True)
    employee         = models.CharField(max_length=100,null=True)
    location         = models.CharField(max_length=100)
    init_date        = models.DateTimeField()
    final_date       = models.DateTimeField()
    reason           = models.CharField(max_length=200)
    date_submitted   = models.DateTimeField(auto_now_add=True)
    status           = models.CharField(max_length = 50,blank=True )