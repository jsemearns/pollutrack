from django.db import models
from django.conf import settings


class ImageUploads(models.Model):
    image_file = models.ImageField(upload_to=settings.IMAGE_UPLOAD_PATH)
    description = models.TextField(blank=True)
