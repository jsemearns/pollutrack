from django.db import models
from django.conf import settings


class ImageUploads(models.Model):
    image_file = models.ImageField(upload_to=settings.IMAGE_UPLOAD_PATH)
    description = models.TextField(blank=True)
    when = models.DateTimeField(auto_now_add=True)

    @property
    def url(self):
        return '/' + self.image_file.url

    class Meta:
        app_label = 'images'
