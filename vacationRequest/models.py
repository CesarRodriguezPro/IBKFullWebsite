from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class vacationRequest(models.Model):
    foreman          = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    employee         = models.CharField(max_length=100,null=True)
    location         = models.CharField(max_length=100)
    init_date        = models.DateTimeField()
    final_date       = models.DateTimeField()
    date_submitted   = models.DateTimeField(auto_now_add=True)
    status           = models.CharField(max_length = 50,blank=True )