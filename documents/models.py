from django.db import models


class Document(models.Model):
    file_name = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name

    def delete(self,*args, **kwargs):
        self.document.delete()
        super().delete(*args, **kwargs)