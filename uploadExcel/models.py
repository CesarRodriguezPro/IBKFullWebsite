from django.db import models
import os
from django.utils.deconstruct import deconstructible

@deconstructible
class PathRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format('data', ext)
        return os.path.join(self.path, filename)

path_and_rename = PathRename("test")


class ExcelUploadModel(models.Model):

    file_name = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to=path_and_rename)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name

    def delete(self,*args, **kwargs):
        self.document.delete()
        super().delete(*args, **kwargs)


