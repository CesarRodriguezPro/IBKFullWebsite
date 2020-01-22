from django.db import models
import os

def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            filename = '{}.{}'.format('data', ext)
        return os.path.join(path, filename)
    return wrapper


class ExcelUploadModel(models.Model):

    file_name = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to=path_and_rename('test/'))
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name

    def delete(self,*args, **kwargs):
        self.document.delete()
        super().delete(*args, **kwargs)


