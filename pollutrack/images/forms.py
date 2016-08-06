from django.forms import ModelForm

from images.models import ImageUploads


class ImageForm(ModelForm):
    class Meta:
        model = ImageUploads
        fields = ['image_file']