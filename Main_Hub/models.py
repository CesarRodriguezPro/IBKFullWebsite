from django.db import models


class CurrentPageModel(models.Model):
    current_page = models.CharField(max_length=20,null=True, blank=True)

    def __str__(self):
        return f'{self.current_page}'


