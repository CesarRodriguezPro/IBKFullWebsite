from django.db import models
from django.urls import reverse


class vacationRequest(models.Model):
    foreman          = models.CharField(max_length=100, null=True, blank=True)
    employee         = models.CharField(max_length=100, null=True)
    location         = models.CharField(max_length=100)
    init_date        = models.DateField()
    final_date       = models.DateField()
    date_submitted   = models.DateTimeField(auto_now_add=True)
    status           = models.CharField(max_length=50, blank=True )
    work_and_pay     = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse('vacationRequest:vacation_viewinfo', kwargs={'pk': self.pk})

